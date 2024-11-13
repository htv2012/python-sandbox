
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':      'My project',
    'author':           'Hai Vu',
    'url':              'url to get it at',
    'download_url':     'where to download',
    'author_email':     'haivu2004@gmail.com',
    'version':          '0.1',
    'install_requires': ['nose'],
    'packages':         ['NAME'],
    'scripts':          [],
    'name':             'projectname'
}

setup(**config)


