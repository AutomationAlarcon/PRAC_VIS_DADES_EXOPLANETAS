import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'exoplanet_catalog.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)
print(df.dtypes)
'''
df1 = df[["Country","Features","2016","2017","2018","2019","2020","2021"]]
x1 = ["United States", "Canada","France", "Germany", "Italy", "Japan", "United Kingdom"]
df_net_generation = df1.loc[(df1["Country"].isin(x1)) & (df1["Features"] == "net generation")]
x = list(df_net_generation["Country"])
print(df_net_generation)
print(x)

df_net_generation['Country'] = df_net_generation['Country'].astype('category')
df_net_generation['Features'] = df_net_generation['Features'].astype('category')
df_net_generation['2016'] = df_net_generation['2016'].astype(float)

print(df_net_generation.dtypes)
'''