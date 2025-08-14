#!/usr/bin/env python

import pandas as pd


def main():
    data_frame = pd.read_json("raw.json")
    groupped_by_name = data_frame.groupby("name")

    print("\nRAW")
    print(data_frame)

    print("\nAGGREGATE")
    # print(groupped_by_name.aggregate([np.sum, np.mean]))
    print(groupped_by_name.aggregate(["count", "sum", "mean"]))


if __name__ == "__main__":
    main()
