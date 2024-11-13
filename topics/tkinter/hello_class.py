#!/usr/bin/env python
# encoding: utf-8
"""
hello_class.py

Created by Hai Vu on 2010-08-09.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from tkinter import *

class HelloApp(object):
    def __init__(self, master):
        config_frame = Frame(master)
        config_frame.grid(row=0, column=0)
        
        b = Button(config_frame, text='Save')
        b.pack()
        b = Button(config_frame, text='Load')
        b.pack()
        
        lb = Listbox(config_frame)
        lb.pack(fill=X)
        rest_frame = Frame(master)
        rest_frame.grid(row=0, column=1)

        row = 0
        Label(rest_frame, text='URI:').grid(row=row, sticky=W)
        self.uri_entry = Entry(rest_frame)
        self.uri_entry.grid(row=row, column=1, columnspan=2)

        row += 1
        Label(rest_frame, text='User:').grid(row=row, sticky=W)
        self.user_entry = Entry(rest_frame)
        self.user_entry.grid(row=row, column=1, columnspan=2)

        row += 1
        Label(rest_frame, text='Password:').grid(row=row, sticky=W)
        self.password_entry = Entry(rest_frame)
        self.password_entry.grid(row=row, column=1, columnspan=2)
        
        row += 1
        b = Button(rest_frame, text='Get',    command=self.do_get)
        b.grid(row=row, column=0)
        b = Button(rest_frame, text='Post',   command=self.do_post)
        b.grid(row=row, column=1)
        b = Button(rest_frame, text='Put',    command=self.do_put)
        b.grid(row=row, column=2)
        b = Button(rest_frame, text='Delete', command=self.do_delete)
        b.grid(row=row, column=3)
        
    def get_input(self):
        self.uri = self.uri_entry.get()
        self.user = self.user_entry.get()
        self.password = self.password_entry.get()
        print(('URI: %s' % self.uri))
        print(('User:password: %s:%s' % (self.user, self.password)))

    def do_get(self):
        self.get_input()

    def do_post(self):
        self.get_input()

    def do_put(self):
        self.get_input()

    def do_delete(self):
        self.get_input()

def main():
    root = Tk()
    hello_app = HelloApp(root)
    root.title('RESTful Now!')
    root.mainloop()

if __name__ == '__main__':
	main()

