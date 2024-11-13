#!/usr/bin/env python

import pandas as pd
import numpy as np

data_frame = pd.read_json('raw.json')
groupped_by_name = data_frame.groupby('name')

print('\nRAW')
print(data_frame)

print('\nAGGREGATE')
print(groupped_by_name.aggregate([np.sum, np.mean]))