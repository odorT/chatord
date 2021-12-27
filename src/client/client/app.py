from settings import *



def output(msg):
    print(msg)


def conn_op(op, **kwargs):
    if op == '/register':
        msg = conn.register(kwargs['username'], kwargs['password'])
        output(msg)

    if op == '/login':
        msg = conn.login(kwargs['username'], kwargs['password'], conn_details)
        output(msg)

    if op == '/logout':
        msg = conn.logout()
        output(msg)

    if op == '/users':
        msg = conn.get_all_users()
        output(msg)

    if op == '/connect':
        peer_conn = conn.get_all_users().get(kwargs['username'], None)
        output(peer_conn)


def help():
    print("""
    /register username password  - to register 
    /login username password     - to login
    /logout                      - to logout
    /users                       - to get all users
    /disconnect username         - stop to chat with user
    /connect username            - start to chat with user
    /help                        - help
    """)


if __name__ == '__main__':
    print("""
        ####################################################
        ##               Welcome to chatord               ##
        ####################################################
        """)
    help()

    while True:
        inp = input('> ')
        if inp.startswith('/'):

            if inp.startswith('/register'):
                try:
                    command, username, password = inp.strip().split()[:3]
                    conn_op(command, username=username, password=password)
                except ValueError:
                    output('Not enough arguments. Please use help')

            if inp.startswith('/login'):
                try:
                    command, username, password = inp.strip().split()[:3]
                    conn_details = {
                        'host': SERVER_HOST,
                        'port': SERVER_PORT
                    }
                    conn_op(command, username=username, password=password, conn_details=conn_details)
                except ValueError:
                    output('Not enough arguments. Please use help')

            if inp.startswith('/logout') or inp.startswith('/users'):
                try:
                    command = inp.strip().split()[0]
                    conn_op(command)
                except ValueError:
                    output('Not enough arguments. Please use help')

            if inp.startswith('/connect') or inp.startswith('/disconnect'):
                try:
                    command, username = inp.strip().split()[:2]
                    conn_op(command, username=username)
                except ValueError:
                    output('Not enough arguments. Please use help')

            if inp.startswith('/help'):
                help()
