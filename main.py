import pandas as pd
from collections import Counter


def new_label(df1):
    df1.loc[(df1['mass'] >= 0.00001) & (df1['mass'] < 0.1), 'type'] = 'mercurian'
    df1.loc[(df1['mass'] >= 0.1) & (df1['mass'] < 0.5), 'type'] = 'Subterran'
    df1.loc[(df1['mass'] >= 0.5) & (df1['mass'] < 2), 'type'] = 'Earth'
    df1.loc[(df1['mass'] >= 2) & (df1['mass'] < 10), 'type'] = 'Super-Earth'
    df1.loc[(df1['mass'] >= 10) & (df1['mass'] < 50), 'type'] = 'Neptunian'
    df1.loc[(df1['mass'] >= 50) & (df1['mass'] < 5000), 'type'] = 'Jovian'
    df1.loc[(df1['mass'] >= 5000), 'type'] = 'Other'


file_path = 'exoplanet.eu_catalog.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)
df1 = df[['name', 'planet_status', 'mass',
          'radius', 'orbital_period','discovered',
          'detection_type', 'molecules','temp_measured',
          'mass_detection_type', 'star_name']]

# Jupyter mass is 317.83 times the mass of earth
# Jupyter radius is 11.2 times the radius of earth

df1['mass'] = df1['mass'] * 317.83
df1['radius'] = df1['radius'] * 11.2

df1['name'] = df1['name'].astype('category')
df1['planet_status'] = df1['planet_status'].astype('category')
df1['detection_type'] = df1['detection_type'].astype('category')
df1['molecules'] = df1['molecules'].astype('category')
df1['mass_detection_type'] = df1['mass_detection_type'].astype('category')
df1['star_name'] = df1['star_name'].astype('category')
print(df1.dtypes)

print(df['planet_status'].value_counts())
print(df['detection_type'].value_counts())
print(df['molecules'].value_counts())
print(df['mass_detection_type'].value_counts())

df2 = df.loc[df['planet_status'] == 'Confirmed']
dis = df2['discovered'].tolist()
print(Counter(dis))

# Exoplanets classification
#Subterran
# (Mars-sized)
# 0.1 — 0.5 ME or 0.4 — 0.8 RE,

# Terran
#(Earth-sized)
#0.5 — 3 ME or 0.8 — 1.6 RE

#Superterran
#(Super-Earth/Mini-Neptunes)
#3 — 10 ME or 1.6 — 2.5 RE

#More categories in: https://www.sciencenews.org/article/kepler-telescope-doubles-its-count-known-exoplanets

# Mars-sized
# 0.5-0.7
# Earth-sized
# 0.7-1.2
# Super-Earth-sized
# 1.2-1.9
# Sub-Neptune-sized
# 1.9-3.1
# Neptune-sized
# 3.1-5.1
# sub-Jupiter-sized
# 5.1-8.3
# Jupiter-sized
# 8.3-13.7
# Super-Jupiter-sized
# 13.7-22.0

new_label(df1)
df3 = df1.loc[df['planet_status'] == 'Confirmed']
df3['type'] = df3['type'].astype('category')
t = df3['type'].tolist()
print(Counter(t))