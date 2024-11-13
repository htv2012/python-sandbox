# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 21:53:06 2016

@author: haiv
"""

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello, <i>world</i>')


def make_app():
    app = tornado.web.Application([
        (r'/', MainHandler),
    ])
    return app


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
