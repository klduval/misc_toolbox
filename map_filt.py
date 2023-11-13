###going to make some of the mappability work in python so it deals with numbers better

import sys
import numpy as np
import pandas as pd


f = pd.read_table(sys.argv [1], header=None)
f.columns = ['chr', 'start', 'end', 'Name', 'map_score']

filt = float(sys.argv[2])

filtered_data = f.loc[f['map_score'] >= filt].copy()

filtered_data.loc[:, 'start'] = filtered_data['start'].astype(int)
filtered_data.loc[:, 'end'] = filtered_data['end'].astype(int)

filtered_data.to_csv(sys.argv[3], header=False, index=False, sep='\t')
