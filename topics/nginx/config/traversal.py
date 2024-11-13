#!/usr/bin/env python3
"""Exercise the traversal functions."""

import nginx_conf_lib

NGINX_CONF = """
http {
    server {
        server_name 127.0.0.1;
        listen 127.0.0.1:49151;
        location /api;
    }
    match monitor_3e796d00-b1fc-48a3-b8d7-9dcc8abb2ad4 {
        status 200-299;
        header X-Response1 = response-value-1;
        body ~ body-value;
    }
}
""".strip()


def visit(directive, parents):
    names = [node.name for node in parents]
    names.append(directive.name)
    print(".".join(names))


def main():
    """Entry"""
    print("\n# Original text")
    print(NGINX_CONF)

    print("\n# Depth First")
    root = nginx_conf_lib.parse(NGINX_CONF)[0]
    nginx_conf_lib.depth_first_traversal(root, visit)

    print("\n# Breadth First")
    nginx_conf_lib.breadth_first_traversal(root, visit)


if __name__ == "__main__":
    main()
