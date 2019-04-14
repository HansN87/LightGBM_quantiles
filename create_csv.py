#!/usr/bin/env python

import pandas as pd
import numpy as np

df = pd.read_hdf('minimal_dataset.h5')

variables = []
variables.append(df['y'].values)

for i in range(15):
    variables.append(df['x'+str(i)].values)

variables.append(df['weight'].values)

fname = 'minimal_dataset.csv'
np.savetxt(fname, variables, delimiter=" ")
