#!/usr/bin/env python
import webbrowser


if __name__ == '__main__':
    browsers = [
        'mozilla',
        'firefox',
        'netscape',
        'galeon',
        'epiphany',
        'skipstone',
        'kfmclient',
        'konqueror',
        'kfm',
        'mosaic',
        'opera',
        'grail',
        'links',
        'elinks',
        'lynx',
        'w3m',
        'windows-default',
        'macosx',
        'safari',
        'google-chrome',
        'chrome',
        'chromium',
        'chromium-browser',
    ]

    available = {True: [], False: []}
    for browser_name in sorted(browsers):
        try:
            browser = webbrowser.get(browser_name)
        except webbrowser.Error:
            available[False].append(browser_name)
        else:
            available[True].append(browser_name)

    print('# Available')
    for name in available[True]:
        print(f'  {name}')
    print()

    print('# Unavailable')
    for name in available[False]:
        print(f'  {name}')
    print()

