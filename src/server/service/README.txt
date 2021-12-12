## API Endpoints  

/user     --  GET   -> all active users from redis
              POST [username, password, conn_details]
                    -> get auth token and add connection details to redis, activate status to online
              PATCH -> remove user from redis, status to offline

/register --  POST [username, password]
                    -> register user and add to database

