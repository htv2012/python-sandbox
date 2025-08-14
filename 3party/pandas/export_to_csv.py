#!/usr/bin/env python

import pandas as pd


def main():
    data_frame = pd.read_json('raw.json')
    data_frame.to_csv('raw.csv', index=False)


if __name__ == '__main__':
    main()
