#!/usr/bin/env python

import cherrypy
from cherrypy.process.plugins import PIDFile
from mako.template import Template
import sqlite3

class Karaoke:
    def __init__(self):
        cherrypy.log('Application started')
        self.indexTemplate = Template(filename='templates/index.html')

    @cherrypy.expose
    def favorites(self, searchterm=''):
        sql = '''
            SELECT users.name, songs.id, songs.title, songs.singer
            FROM users, favorites, songs
            WHERE
                favorites.uid = users.uid
                AND favorites.sid = songs.id'''
        if searchterm != '':
            sql += ' AND users.name LIKE "{}"'.format(searchterm)
        sql += ' ORDER BY users.name, songs.title'

        self.conn = sqlite3.connect('karaoke.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        headers = ['Name', 'Key', 'Title', "Singers"]
        html = self.indexTemplate.render(data=data, headers=headers, pagetitle='Favorites')
        self.conn.close()
        self.conn = None
        return html

    def __add_search_term(self, searchterm):
        where = ' WHERE '
        tokens = [token.strip() for token in searchterm.split('=')]
        tokens_count = len(tokens)
        if searchterm == '':
            where = ' ORDER BY title, singer'
        elif tokens[0] == 's' and tokens_count == 2:
            where += 'singer LIKE "%{}%"'.format(tokens[1])
            where += ' ORDER BY singer, title'
        elif tokens[0] == 't' and tokens_count == 2:
            where += 'title LIKE "%{}%"'.format(tokens[1])
            where += ' ORDER BY title, singer'
        elif tokens_count == 1:
            where += 'title LIKE "%{0}%" OR singer LIKE "%{1}%"'.format(
                    tokens[0], tokens[0])
            where += ' ORDER BY title, singer'
        else:
            where = ' ORDER BY title, singer'
        return where

    @cherrypy.expose
    def help(self):
        self.helpTemplate = Template(filename='templates/help.html')
        html = self.helpTemplate.render(pagetitle='Karaoke Help')
        return html

    @cherrypy.expose
    def index(self, searchterm=''):
        sql = 'SELECT id, title, singer FROM songs'
        if searchterm == '':
            sql += ' ORDER BY id'
        else:
            sql += self.__add_search_term(searchterm)

        # BUG: why can't I init conn and cursor in __init__() ?
        # When I did so, I got threading problem
        self.conn = sqlite3.connect('karaoke.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        headers = ['Key', 'Title', 'Singers']
        pagetitle='Karaoke Full Listing'
        html = self.indexTemplate.render(
            data=data,
            headers=headers,
            pagetitle=pagetitle)
        self.conn.close()
        self.conn = None
        return html

        
if __name__ == '__main__':
    # Save the PID of this process into a file, this file will be deleted upon
    # app exit
    PIDFile(cherrypy.engine, '/tmp/karaoke.pid').subscribe()
    cherrypy.quickstart(Karaoke(), config='app.config')
