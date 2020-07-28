# https://severalnines.com/blog/mysql-docker-building-container-image
# https://www.percona.com/doc/percona-repo-config/percona-release.html
# https://www.percona.com/doc/percona-repo-config/percona-release.html#percona-release-usage
storagePath=/home/u/r07946014/storage/mysql/weidao-mysql
dockerImage=mysql:latest
containerName=weidao-mysql

mkdir -p $storagePath

docker run \
	   -dit \
	   --rm \
	   --name $containerName \
	   -p 8013:3306 \
	   -e MYSQL_ROOT_PASSWORD=root \
	   -v $storagePath:/var/lib/mysql \
	   $dockerImage
