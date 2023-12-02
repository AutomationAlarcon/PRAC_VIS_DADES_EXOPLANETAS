import pandas as pd

file_path = 'exoplanet_catalog.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)
datatype = df.dtypes
obj_column = datatype[datatype == 'object'].index.tolist()
print(obj_column)
