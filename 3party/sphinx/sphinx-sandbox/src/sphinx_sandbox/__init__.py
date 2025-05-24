def connect(conn_str: str, user: str):
    """Connect to a database.

    This function is under construction.

    :param conn_str: Connection string, such as "mydb://127.0.0.1:9999".
        If connection string does not include a port, a default port are used.
        An empty connection string means the default host and port are used.
    :param user: User alias
    :returns: A connection object
    """
    pass


def main():
    """Package entry."""
    print("Hello from sphinx-sandbox!")
