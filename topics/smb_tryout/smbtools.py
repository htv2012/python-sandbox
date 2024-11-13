#!/usr/bin/env python

import os
import platform
import contextlib
import time


# Determine the current platform
system = platform.system()
is_mac = (system == 'Darwin')
is_windows = (system == 'Windows')


@contextlib.contextmanager
def mount(url, timeout=30):
    # Remove trailing slashes
    while url[-1] in {'/', '\\'}:
        url = url[:-1]

    if is_mac:
        mount_dir = os.path.join('/Volumes', os.path.split(url)[-1])
        os.mkdir(mount_dir)
        os.system('mount -t smbfs {} {}'.format(url, mount_dir))

        # Wait for mount
        for _ in range(timeout):
            if os.path.exists(mount_dir):
                break
            time.sleep(1)
        else:
            # Timed out
            raise IOError('Failed to mount {} to {}'.format(url, mount_dir))
    elif is_windows:
        mount_dir = url

    yield mount_dir

    if is_mac:
        os.system('umount {}'.format(mount_dir))



# def smb_upload(local_file, host, share, remote_path):
#
#     remote_dir = 'smb://{}/{}/{}'.format(host, share, remote_path)

def upload(local_files, url):
    pass

if __name__ == '__main__':
    smb_upload(local_file=__file__, host='dakao.local', share='temp', remote_path='/foo/bar')

