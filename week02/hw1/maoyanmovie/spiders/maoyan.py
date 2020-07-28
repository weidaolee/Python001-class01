import scrapy
from maoyanmovie.items import MaoyanmovieItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = [
        'https://maoyan.com/films?showType=3',
    ]

    cookies = '__mta=214726952.1593850009964.1593880344744.1593887067516.13; uuid_n_v=v1; uuid=509181C0BDCD11EAB5685D560D8487BBFF7A2266D34C4BB8B540F427E88AC6EC; mojo-uuid=fb15aa44a9d0606a427d2666a03b10e6; _lxsdk_cuid=17318dd18a6c8-0c688aa49ea96b-4353760-144000-17318dd18a6c8; _lxsdk=509181C0BDCD11EAB5685D560D8487BBFF7A2266D34C4BB8B540F427E88AC6EC; _csrf=c68410e1dffa159c75a1110784b8b72fd47226979a582aa610a344e94483fc56; mojo-session-id={"id":"8b158aa2d052e1516494ff252f91fe55","time":1595917134668}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593881215,1595489436,1595498105,1595917135; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595917135; __mta=214726952.1593850009964.1593887067516.1595917135930.14; _lxsdk_s=1739412ec57-c45-ed6-636%7C%7C2'.split(
        '; ')

    cookies = dict([s.split('=') for s in cookies])

    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url,
                             callback=self.get_target_urls,
                             cookies=self.cookies)

    def get_target_urls(self, response):
        item = MaoyanmovieItem()
        movies = scrapy.Selector(response).xpath(
            '//div[@class="channel-detail movie-item-title"]')
        for m in movies[:10]:
            href = m.xpath('./a/@href').extract_first()

            url = f'https://maoyan.com{href}'
            # item['Link'] = url
            yield scrapy.Request(url,
                                 callback=self.get_movie_info,
                                 cookies=self.cookies,
                                 meta={'item': item})

    def get_movie_info(self, response):
        item = response.meta['item']

        container = scrapy.Selector(response).xpath(
            '//div[@class="movie-brief-container"]')
        ul = container.xpath('./ul')

        item['Name'] = container.xpath('./h1/text()')
        item['Type'] = ul.xpath('./li[1]//a/text()')
        item['Date'] = ul.xpath('./li[last()]/text()')

        yield item
