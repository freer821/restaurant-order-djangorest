docker build . -t whs

docker run -it -d -e WHS_ENV='test' --name whs -p 9001:80 -v /home/ubuntu/work/projects/python/whsys:/application  --link ub-mariadb:ub-mariadb whs
