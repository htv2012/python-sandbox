#!/usr/bin/env python
""" static method """


class Server:
    """Base class"""

    @staticmethod
    def login():
        """Demo function"""
        print("login")

    @staticmethod
    def logout():
        """Demo function"""
        print("logout")


class MyServer(Server):
    """Child class"""

    @staticmethod
    def enter_password():
        """Demo function"""
        print("enter_password")


def main():
    """Entry"""
    MyServer.login()
    MyServer.enter_password()
    MyServer.logout()


if __name__ == "__main__":
    main()
