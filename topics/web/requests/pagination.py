#!/usr/bin/env python3
"""
whatis: Make API GET call, with pagination
"""
import json

import requests


if __name__ == '__main__':
    url = 'https://reqres.in/api/users?per_page=5&page={}'
    template = 'ID = {0[id]:>2}: {0[first_name]} {0[last_name]}'

    # Start with page 1 and assume 2 pages. As we go along, we will
    # update total_pages based on the JSON returned by the system.
    page = 1
    total_pages = 2

    while page <= total_pages:
        response = requests.get(url.format(page))
        data = response.json()
        print('--- Page {} ---'.format(data['page']))

        for record in data['data']:
            print(template.format(record))

        total_pages = data['total_pages']
        page += 1

