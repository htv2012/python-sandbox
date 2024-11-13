"""
whatis: Try out http.server
"""
import http.server
import logging
import multiprocessing
import os
import time
import unittest
import urllib.error
import urllib.parse
import urllib.request


logging.basicConfig(level=os.getenv('LOGLEVEL', 'WARN'))


class HTTPFileServer:
    """
    A simple HTTP file server
    """
    def __init__(self, dir_path, port=9999):
        self._dir_path = dir_path
        self._port = port
        self.server = None
        self.logger = logging.getLogger('HTTPFileServer')

    def async_start(self):
        """
        Starts the server asynchronously
        """
        self.logger.info('Starting service')
        self.server = multiprocessing.Process(target=self.serve)
        self.server.daemon = True
        self.server.start()
        time.sleep(1)
        self.logger.info('Service started')

    def serve(self):
        """
        Creates a server object and serve forever
        """
        os.chdir(self._dir_path)
        self.logger.info('Chdir to %s', self._dir_path)
        httpd = http.server.HTTPServer(
            ('', self._port),
            http.server.SimpleHTTPRequestHandler)
        self.logger.info('httpd: %s', httpd)
        self.logger.info('Serving at port %d', self._port)
        httpd.serve_forever()


class MyTest(unittest.TestCase):
    """
    Test the HTTPFileServer class
    """
    @classmethod
    def setUpClass(cls):
        test_dir = os.path.dirname(__file__) or '.'
        cls.web_server = HTTPFileServer(test_dir)
        cls.web_server.async_start()

    def test_get_file(self):
        """
        Simple GET test
        """
        url = 'http://localhost:9999/hello.txt'
        response = urllib.request.urlopen(url)
        self.assertEqual(200, response.code)
        text = response.read().decode('utf-8')
        self.assertEqual('hello world\n', text)


if __name__ == '__main__':
    unittest.main()
