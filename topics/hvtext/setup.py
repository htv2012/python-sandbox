#!/usr/bin/env python
"""
Setup for hvtext
"""
from setuptools import setup, find_packages


setup(
    name='hvtext',
    version='0.1.0',
    author='Hai Vu',
    author_email='haivu2004@gmail.com',
    packages=find_packages(),
    url='http://pypi.python.org/pypi/hvtext/',
    license='LICENSE.txt',
    description='A collection of text-processing tools',
    long_description=open('README.md').read(),
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: General',
        'Environment :: Console',
    ]
)

