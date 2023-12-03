import pandas as pd

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

print(df1.dtypes)

print(df['planet_status'].value_counts())
print(df['detection_type'].value_counts())
print(df['molecules'].value_counts())
print(df['mass_detection_type'].value_counts())

