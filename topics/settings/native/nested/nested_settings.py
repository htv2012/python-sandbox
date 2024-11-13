import settings
import settings.users

import settings as config

def main():
    print('Server')
    print('  Host: %s' % settings.server)
    print('  Port: %d' % config.port)

    print('Users')
    print('  Admin user: %s' % settings.users.admin_user)
    print('  Admin password: %s' % settings.users.admin_password)


if __name__ == '__main__':
    main()

