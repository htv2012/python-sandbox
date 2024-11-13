#!/usr/bin/env python

import os
import sys
import subprocess
import tempfile


def get_load_name(line):
    """
    Given: a string such as
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 125.2.0)

    Return: the load_name, such as:
        /usr/lib/libSystem.B.dylib
    """

    load_name_ends_at = line.find(' (')
    if load_name_ends_at < 0:
        return ''
    else:
        return line[:load_name_ends_at].strip()

# TODO: need better name
def change(dylib_filename, old_path, new_dylib_filename):
    new_path = os.path.join(new_dylib_filename, os.path.split(old_path)[1])
    args = [ 'install_name_tool', '-change', old_path, new_path, dylib_filename ]
    print(' '.join(args))
    exit_code = subprocess.call(args)
    return exit_code

# TODO: need better name
def change_all(dylib_filename):
    args = ['otool', '-L', dylib_filename]
    output = tempfile.TemporaryFile()
    subprocess.check_call(args, stdout=output)
    output.seek(0)

    for line in output:
        old_path = get_load_name(line)
        # TODO: How do we know which old_path need to be replaced? Searching for
        # 'movi' is just a wild guess. Talk to Jason.
        if old_path.find('movi') >= 0:
            change(dylib_filename, old_path, '@executable_path/../Frameworks')

    output.close()


if __name__ == '__main__':
    change_all(sys.argv[1])
        
"""
Sample otool output:
$ otool -L libpme.0.dylib
libpme.0.dylib:
	@executable_path/../Frameworks/libpme.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	@executable_path/../Frameworks/libgstapp-0.10.0.dylib (compatibility version 25.0.0, current version 25.0.0)
	/System/Library/Frameworks/Security.framework/Versions/A/Security (compatibility version 1.0.0, current version 37594.0.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 125.2.0)
	/usr/lib/libxml2.2.dylib (compatibility version 10.0.0, current version 10.3.0)
	@executable_path/../Frameworks/libgio-2.0.dylib (compatibility version 2702.0.0, current version 2702.0.0)
	/usr/lib/libresolv.9.dylib (compatibility version 1.0.0, current version 41.0.0)
	/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.3)
	/System/Library/Frameworks/OpenAL.framework/Versions/A/OpenAL (compatibility version 1.0.0, current version 1.0.0)
	/System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio (compatibility version 1.0.0, current version 1.0.0)
	/System/Library/Frameworks/AudioUnit.framework/Versions/A/AudioUnit (compatibility version 1.0.0, current version 1.0.0)
	/System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices (compatibility version 1.0.0, current version 44.0.0)
	@executable_path/../Frameworks/libgstaudio-0.10.0.dylib (compatibility version 25.0.0, current version 25.0.0)
	@executable_path/../Frameworks/libgstpbutils-0.10.0.dylib (compatibility version 25.0.0, current version 25.0.0)
	@executable_path/../Frameworks/libtaagsth264codecbase.0.dylib (compatibility version 1.0.0, current version 1.0.0)
	@executable_path/../Frameworks/libgstinterfaces-0.10.0.dylib (compatibility version 25.0.0, current version 25.0.0)
	/Users/cpvedev/cpve_trunk/movi/src/tetris/build/i386-darwin/lib/libssl.0.9.8.dylib (compatibility version 0.9.8, current version 0.9.8)
	/Users/cpvedev/cpve_trunk/movi/src/tetris/build/i386-darwin/lib/libcrypto.0.9.8.dylib (compatibility version 0.9.8, current version 0.9.8)
	@executable_path/../Frameworks/libgstrtp-0.10.0.dylib (compatibility version 25.0.0, current version 25.0.0)
	@executable_path/../Frameworks/libgstbase-0.10.0.dylib (compatibility version 30.0.0, current version 30.0.0)
	/usr/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.9.0)
	@executable_path/../Frameworks/libgstreamer-0.10.0.dylib (compatibility version 30.0.0, current version 30.0.0)
	@executable_path/../Frameworks/libgobject-2.0.dylib (compatibility version 2702.0.0, current version 2702.0.0)
	@executable_path/../Frameworks/libgmodule-2.0.dylib (compatibility version 2702.0.0, current version 2702.0.0)
	@executable_path/../Frameworks/libgthread-2.0.dylib (compatibility version 2702.0.0, current version 2702.0.0)
	@executable_path/../Frameworks/libglib-2.0.dylib (compatibility version 2702.0.0, current version 2702.0.0)
	/usr/lib/libiconv.2.dylib (compatibility version 7.0.0, current version 7.0.0)
	/System/Library/Frameworks/Carbon.framework/Versions/A/Carbon (compatibility version 2.0.0, current version 152.0.0)
	/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 550.29.0)
	/System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices (compatibility version 1.0.0, current version 38.0.0)
"""
