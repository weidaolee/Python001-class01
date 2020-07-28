import pymysql
from maoyanmovie.user import dbInfo
# Connect to the database

class ConnDB(object):
    def __init__(self, dbInfo):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    def creat_table(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
        )
        sql_command = \
        '''CREATE TABLE IF NOT EXISTS 
        maoyan (
        id INT(10) AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
        Type VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
        Date DATE NOT NULL)
        DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
'''
        try:
            with conn.cursor() as cur:
                cur.execute(sql_command)
            conn.commit()
            print('success.')

        except pymysql.InternalError as error:
            code, message = error.args
            print('>>>>>>', code, message)
            conn.rollback()

        conn.close()

    def insert(self, data):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
        )

        name_ = data['Name'][0]
        type_ = data['Type'][0]
        date_ = data['Date'][0]
        print(name_)
        print(type_)
        print(date_)

        sql_command = \
        '''
        INSERT INTO maoyan (Name, Type, Date)
        VALUES (%s, %s, %s)
        '''

        try:
            with conn.cursor() as cur:
                cur.execute(sql_command, (name_, type_, date_))
            conn.commit()
            print('success.')

        except pymysql.InternalError as error:
            code, message = error.args
            print('>>>>>>', code, message)
            conn.rollback()

        conn.close()


if __name__ == '__main__':
    db = ConnDB(dbInfo)
    db.creat_table()
