docker build . -t whsys

docker run -it -d -e WHS_ENV='test' --name whs -p 8001:80 -v /home/ubuntu/work/projects/python/whsys:/home/docker/code/app  --link ub-mariadb:ub-mariadb whs
docker run -it -d -e WHS_ENV='prod' --name whsys -p 8005:80 -v /home/root/work/whsys:/home/docker/code/app  --link ub-mariadb:ub-mariadb whsys
