# chatord
Peer to Peer chat application using sockets, curses and RESTFul
 
* for creating docker network, use command below:
```shell
docker network create --driver=bridge --subnet=192.168.0.0/24 --ip-range=192.168.0.1/29 --gateway=192.168.0.6 app-network
```

* then run following
```shell
docker-compose build
docker-compose up
```

API is exposed at: localhost:80  
MYSQL is exposed at: localhost:3306  
REDIS is exposed at: localhost:6379
