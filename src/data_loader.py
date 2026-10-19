import pandas as pd
import numpy as np

df1=pd.read_csv('data/exoplanets.csv')

for i in range(df1.shape[0]):
    for j in df1.iloc[i]:
        if j==np.nan:
            del df1.iloc[i]

df1=df1


def load_data():
    return df1





