
clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    clients += client_name
    _add_comma()

def _add_comma():
    global clients
    
    clients += ','

if __name__ == '__main__':
    create_client('Luis')
    print(clients)
