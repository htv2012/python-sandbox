"""
Windows Registry Tools
"""
import collections
import contextlib
import itertools
import platform

if platform.system() != 'Windows':
    raise OSError('This module only works with Windows')

import winreg


RESERVED = 0
top_nodes = dict(
    HKCU=winreg.HKEY_CURRENT_USER,
    HKEY_CURRENT_USER=winreg.HKEY_CURRENT_USER,
)

class Registry(collections.MutableMapping):
    def __init__(self, top_node, path):
        self.top_node = top_node
        self.path = path

        try:
            with self._open_key():
                pass
        except WindowsError:
            raise ValueError('Invalid path: {!r}'.format(path))

    @classmethod
    def from_path(cls, path):
        DRIVE_SEPARATOR = ':\\'
        if DRIVE_SEPARATOR not in path:
            raise ValueError('Invalid path: {!r}'.format(path))
        top_node, path = path.split(DRIVE_SEPARATOR)

        if top_node not in top_nodes:
            raise ValueError('Invalid top node: {!r}'.format(top_node))
        top_node = top_nodes[top_node]

        new_registry = cls(top_node, path)
        return new_registry

    @contextlib.contextmanager
    def _open_key(self, permission=winreg.KEY_READ):
        key = winreg.OpenKey(self.top_node, self.path, RESERVED, permission)
        yield key
        winreg.CloseKey(key)

    def __getitem__(self, key):
        try:
            with self._open_key() as container:
                value, data_type = winreg.QueryValueEx(container, key)
                return value
        except WindowsError:
            key_path = '{}\\{}'.format(self.path, key)
            raise KeyError(key_path)

    def __setitem__(self, key, value):
        if isinstance(value, str):
            data_type = winreg.REG_SZ
        elif isinstance(value, int):
            data_type = winreg.REG_DWORD
        else:
            raise TypeError('Cannot handle object of type {}'.format(type(value).__name__))

        with self._open_key(winreg.KEY_WRITE) as container:
            winreg.SetValueEx(container, key, RESERVED, data_type, value)

    def __delitem__(self, key):
        with self._open_key(winreg.KEY_WRITE) as container:
            winreg.DeleteValue(container, key)

    def __iter__(self):
        with self._open_key() as container:
            try:
                for key_number in itertools.count():
                    name, value, data_type = winreg.EnumValue(container, key_number)
                    yield name
            except WindowsError:
                pass

    def __len__(self):
        with self._open_key() as container:
            _, values_count, _ = winreg.QueryInfoKey(container)
            return values_count


if __name__ == '__main__':
    r = Registry.from_path('HKCU:\\Software\\Sandbox')

    r['DeleteMe'] = 1

    print('--- Before')
    for k, v in list(r.items()):
        print('    {} = {!r}'.format(k, v))

    r['StringValue'] = 'Modified String Value'
    r['DwordValue'] = 1234
    del r['DeleteMe']

    print('\n--- After')
    for k, v in list(r.items()):
        print('    {} = {!r}'.format(k, v))


    # value = r['WarnUpgrade20Save2']
