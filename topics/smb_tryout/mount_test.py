#!/usr/bin/env python


import os

import smbtools

if __name__ == "__main__":
    url = "smb://dakao/temp/foo"
    with smbtools.mount(url) as mount_dir:
        print("Mounting {} to local dir: {}".format(url, mount_dir))
        print("Files list:")
        for filename in os.listdir(mount_dir):
            print(filename)
