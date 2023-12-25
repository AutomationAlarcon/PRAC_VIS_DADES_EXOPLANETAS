import pandas as pd
from collections import Counter


def set_data_column_mass(text1, text2):
    """
    This method is to create a new column from a dataframe.
    The values are for the mass classification of exoplanets in: https://www.space.com/36935-planet-classification.html
    Parameters:
        text1 (str): The name of a column.
        text2 (str): The name of a new column.

    returns:
        The same dataframe, but with a new column.
    """

    df1.loc[(df1[text1] >= 0.00001) & (df1[text1] <= 0.1), text2] = 'mercurian'
    df1.loc[(df1[text1] > 0.1) & (df1[text1] <= 0.5), text2] = 'Subterran'
    df1.loc[(df1[text1] > 0.5) & (df1[text1] <= 2), text2] = 'Earth'
    df1.loc[(df1[text1] > 2) & (df1[text1] <= 10), text2] = 'Super-Earth'
    df1.loc[(df1[text1] > 10) & (df1[text1] <= 50), text2] = 'Neptunian'
    df1.loc[(df1[text1] > 50) & (df1[text1] <= 5000), text2] = 'Jovian'
    df1.loc[(df1[text1] > 5000), text2] = 'Super-Jovian'


def actions_mass_classification(text1, text2):
    """
    This method is to do actions with a dataframe with a column with data
    about mass classification.
    Parameters:
        text1 (str): The name of a column.
        text2 (str): The name of a new column.

    returns:
        The same dataframe, but with a new column and some actions.
    """

    set_data_column_mass(text1, text2)
    df1[text2] = df1[text2].astype('category')
    print(df1.dtypes)
    t = df1[text2].tolist()
    print(t)

    t_values = [i for i in dict(Counter(t)).values()]
    t_keys = list(dict(Counter(t)).keys())
    print(t_values)
    print(t_keys)


def set_data_column_radius_reduced(text1, text2):
    """
    This method is to create a new column from a dataframe.
    The values are for radius classification of exoplanets.
    In this case is for the reduced classification in: https://phl.upr.edu/projects/habitable-exoplanets-catalog
    Parameters:
        text1 (str): The name of a column.
        text2 (str): The name of a new column.

    returns:
        The same dataframe, but with a new column.
    """

    df1.loc[(df1[text1] < 0.4), text2] = 'Like-mercurian'
    df1.loc[(df1[text1] >= 0.4) & (df1[text1] <= 0.8), text2] = 'Subterran'
    df1.loc[(df1[text1] >= 0.8) & (df1[text1] <= 1.6), text2] = 'Terran'
    df1.loc[(df1[text1] >= 1.6) & (df1[text1] <= 2.5), text2] = 'Superterran'
    df1.loc[(df1[text1] > 2.5), text2] = 'Like-jovian'


def actions_radius_reduced_classification(text1, text2):
    """
    This method is to do actions with a dataframe with a column with data
    about radius reduced classification.
    Parameters:
        text1 (str): The name of a column.
        text2 (str): The name of a new column.

    returns:
        The same dataframe, but with a new column and some actions.
    """

    set_data_column_radius_reduced(text1, text2)
    df1[text2] = df1[text2].astype('category')
    print(df1.dtypes)
    t = df1[text2].tolist()

    t_values = [i for i in dict(Counter(t)).values()]
    t_keys = list(dict(Counter(t)).keys())
    print(t_values)
    print(t_keys)


def get_value_counts():
    """
    This method is to do get some value counts from a database.

    returns:
        Print the values.
    """
    print(df1['planet_status'].value_counts())
    print(df1['detection_type'].value_counts())
    print(df1['molecules'].value_counts())
    print(df1['mass_detection_type'].value_counts())


def get_data_year_discovered():
    """
    This method is to do get the data of the discovered year.

    returns:
        Print the values.
    """

    dis = df1['discovered'].tolist()
    print(Counter(dis))


# source: https://exoplanet.eu/catalog/all_fields/
file_path = 'exoplanet.eu_catalog.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)

df1 = df[['name', 'planet_status', 'mass',
          'radius', 'orbital_period','discovered',
          'detection_type', 'molecules','temp_measured',
          'mass_detection_type', 'star_name']]

# Data are in Jupyter reference:
#   - Jupyter mass is 317.83 times the mass of earth
#   - Jupyter radius is 11.2 times the radius of earth

df1['mass'] = df1['mass'] * 317.83
df1['radius'] = df1['radius'] * 11.2

df1['name'] = df1['name'].astype('category')
df1['planet_status'] = df1['planet_status'].astype('category')
df1['detection_type'] = df1['detection_type'].astype('category')
df1['molecules'] = df1['molecules'].astype('category')
df1['mass_detection_type'] = df1['mass_detection_type'].astype('category')
df1['star_name'] = df1['star_name'].astype('category')
print(df1.dtypes)

df1 = df1.loc[df1['planet_status'] == 'Confirmed']
# get_value_counts()
# get_data_year_discovered()
# actions_mass_classification('mass', 'type_mass')
# actions_radius_reduced_classification('radius', 'type_radius')
