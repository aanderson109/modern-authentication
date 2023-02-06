Basic example of a TCP client/server network
* uses python's socket and threading libraries

Server leverages instances of a client object and individual threads to listen to incoming data from each client while listening for new connections.

## how to run
1. run `server.py`
    - input a host and port for the server when prompted
        __tip__: if you are running the client on the same computer or local network, use `localhost` as the host name.
        __tip__: port can be any 16-bit number lower than 65535 but must be forwarded on your router if the client is on a different network.

2. run `client.py`
    - if the server is running on the same computer, use `localhost` as the host

