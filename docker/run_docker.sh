docker build . -t whs

docker run -it -d -e WHS_ENV='test' --name whs -p 8001:80 -v /home/ubuntu/work/projects/python/whsys:/home/docker/code/app  --link ub-mariadb:ub-mariadb whs
