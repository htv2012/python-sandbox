#!/usr/bin/env python

import json
import collections
from pprint import pprint

if __name__ == '__main__':    
    # Load file into data
    with open('raw.json') as f:
        data = [json.loads(line) for line in f]

    # Calculate count and total
    time_total = collections.defaultdict(float)
    time_count = collections.defaultdict(int)
    for row in data:
        time_count[row['name']] += 1
        time_total[row['name']] += row['time']
        
    # Calculate average
    time_average = {}
    for name in time_count:
        time_average[name] = time_total[name] / time_count[name]
        
    # Report
    for name in sorted(time_count):
        print('{:<10} {:2} {:8.2f} {:8.2f}'.format(
            name,
            time_count[name],
            time_total[name],
            time_average[name]))
            
    # Filter data: prints all rows with 'machine5'
    print('\nFilter by machine5')
    machine5 = [row for row in data if row['name'] == 'machine5']
    machine5 = sorted(machine5, key=lambda row: int(row['time']))
    pprint(machine5)
    
    # Get the last instance
    print('\nLast instance of machine5:')
    latest_row = machine5[-1]
    pprint(latest_row)