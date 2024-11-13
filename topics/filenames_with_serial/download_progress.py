#!/usr/bin/env python

import sqlite3
import sys
import os
import collections
import re


class Tally(object):
    title_episode_pattern = re.compile(r'(.+)_0*(\d+)\w*\.\w+')

    def __init__(self, root):
        self.root = root

        try:
            os.remove('tally.db')
        except OSError:
            pass
        self.db = sqlite3.connect('tally.db')
        self.create_tables()

    def create_tables(self):
        sql = '''
            CREATE TABLE download (
                title TEXT,
                episode INT
            )
        '''
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()

    def tally(self):
        for dirpath, dirnames, filenames in os.walk(self.root):
            list(map(self.add_file, filenames))

    def parse_filename(self, filename):
        match = re.search(Tally.title_episode_pattern, filename)
        if match:
            title, episode = match.groups()
            episode = int(episode)
        else:
            title = filename
            episode = -1
        return title, episode

    def add_file(self, filename):
        parts = self.parse_filename(filename)
        sql = 'INSERT INTO download VALUES (?, ?)'
        cursor = self.db.cursor()
        cursor.execute(sql, parts)
        self.db.commit()

    def report(self):
        sql = '''
            SELECT title, COUNT(episode), MAX(episode)
            FROM download
            WHERE episode != -1
            GROUP BY title
        '''
        cursor = self.db.cursor()
        cursor.execute(sql)
        for title, count, last in cursor:
            missing = self.find_missing(title, last)
            print('{:<24} {:3}'.format(title, last), end=' ')
            if missing:
                print(' missing:', ', '.join(str(e) for e in missing), end=' ')
            print('')

    def find_missing(self, title, last):
        sql = '''
            SELECT episode
            FROM download
            WHERE title = ?
        '''
        cursor = self.db.cursor()
        cursor.execute(sql, (title,))
        episodes = set(e for (e,) in cursor)
        all_episodes = set(range(1, last+1))
        missing = all_episodes - episodes
        return sorted(missing)

def main():
    root_dir = '/Volumes/haibo/do_not_back_up/Videos/Samples'
    tally = Tally(root_dir)
    tally.tally()
    tally.report()



if __name__ == '__main__':
    main()