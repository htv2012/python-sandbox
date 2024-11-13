#!/usr/bin/env python

import pandas as pd


if __name__ == '__main__':
    data_frame = pd.read_json('raw.json')
    data_frame.to_csv('raw.csv', index=False)
