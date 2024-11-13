#!/usr/bin/env python



import os
import socket
import urllib.request, urllib.error, urllib.parse
from smb.SMBHandler import SMBHandler

class Samba(object):
    def __init__(self, host, share, user=None, password=None):
        self.host = host
        self.share = share
        self.user = user
        self.password = password
        try:
            self.host_ip = socket.gethostbyname(host)
        except socket.gaierror:
            print('Host is not reachable: {}'.format(host))
            raise

    def upload(self, local_filename, remote_dir, new_filename=None):
        # Remove slashes on both end, this block is a hack, not entirely foolproof
        if remote_dir.startswith('/'):
            remote_path = remote_dir[1:]
        if remote_dir.endswith('/'):
            remote_dir = remote_dir[:-1]

        basename = new_filename or os.path.basename(local_filename)
        remote_path = remote_dir + '/' + basename

        url = 'smb://{}/{}/{}'.format(self.host_ip, self.share, remote_path)
        director = urllib.request.build_opener(SMBHandler)
        with open(local_filename, 'rb') as f:
            remote_file_handler = director.open(url, data=f)
            remote_file_handler.close()


def upload(local_files, remote_dir):
    director = urllib.request.build_opener(SMBHandler)
    raise NotImplementedError('Do the rest')


def main():
    smb = Samba('dakao.local', 'temp')
    smb.upload(local_filename='upload.py', remote_dir='/foo/bar/')
if __name__ == '__main__':
    main()

