import pandas as pd
from collections import Counter
from openpyxl.workbook import Workbook
import seaborn as sns
import matplotlib.pyplot as plt


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


def get_data_year_discovered():
    """
    This method is to do get the data of the discovered year.

    returns:
        Print the values.
    """

    dis = df1['discovered'].tolist()
    print(Counter(dis))


def flatten(xss):
    """
    This method is to flat a list with various lists inside.

    returns:
        A list of elements.
    """
    return [x for xs in xss for x in xs]


def get_molecules_values():
    """
    This method is to get a list with the molecules.

    returns:
        A list of molecules.
    """
    t = df1['molecules'].tolist()
    t_values = [i for i in dict(Counter(t)).values()]
    t_keys = list(dict(Counter(t)).keys())
    print(t_values)
    print(t_keys)
    mol = []
    for k in t_keys:
        if str(k) != 'nan':
            mol.append(str(k).split(','))
    print(Counter(flatten(mol)))


# Data source: https://exoplanet.eu/catalog/all_fields/
file_path = 'exoplanet.eu_catalog.csv'
df = pd.read_csv(file_path, sep=",", skipinitialspace=True)

df1 = df[['name', 'planet_status', 'mass',
          'radius', 'orbital_period','discovered',
          'detection_type', 'molecules','temp_measured',
          'mass_detection_type', 'star_name']]



df1['name'] = df1['name'].astype('category')
df1['planet_status'] = df1['planet_status'].astype('category')
df1['detection_type'] = df1['detection_type'].astype('category')
df1['molecules'] = df1['molecules'].astype('category')
df1['mass_detection_type'] = df1['mass_detection_type'].astype('category')
df1['star_name'] = df1['star_name'].astype('category')
print(df1.dtypes)

print("                    ")
print("GET EXOPLANET STATUS")
print("                    ")
print(df1['planet_status'].value_counts())

print("                        ")
print("GET THE MOLECULES VALUES")
print("                        ")
get_molecules_values()

print("                                   ")
print("GET THE DATA FOR THE BUBBLE DIAGRAM")
print("                                   ")
print("Selection for confirmed exoplanets")
df1 = df1.loc[df1['planet_status'] == 'Confirmed']

print("Original data have Jupyter reference. Change data reference from Jupyter to Earth")
# Data are in Jupyter reference:
#   - Jupyter mass is 317.83 times the mass of earth
#   - Jupyter radius is 11.2 times the radius of earth
df1['mass'] = df1['mass'] * 317.83
df1['radius'] = df1['radius'] * 11.2

print("Set the value of the radius=1.1 for Proxima Centauri b")
df1.loc[(df1['name'] == 'Proxima Centauri b'), 'radius'] = 1.1

print("Create a classification based on the exoplanet radius")
actions_radius_reduced_classification('radius', 'type_radius')
print("Selection os the column for the bubble diagram")
df2 = df1[['name', 'radius', 'orbital_period', 'mass', 'type_radius']]
print("Remove the rows with nan values")
filtered_df = df2[df2[['name', 'radius', 'orbital_period', 'mass', 'type_radius']].notnull().all(1)]
print("Selection of the like-terran exoplanets")
filtered_df = filtered_df.loc[(filtered_df['type_radius'] == 'Terran') | (filtered_df['type_radius'] == 'Superterran') |
                              (filtered_df['type_radius'] == 'Subterran')]
print("Select values for earth planet")
filtered_df.loc[len(filtered_df.index)] = ['Earth', 1, 1, 365, 'Terran']

print("Detect outliers values")
sns.boxplot(filtered_df['mass'])
plt.tight_layout()
plt.savefig("mass", dpi=100, bbox_inches='tight')
plt.close()
filtered_df = filtered_df.loc[filtered_df['mass'] < 5.00]

sns.boxplot(filtered_df['orbital_period'])
plt.tight_layout()
plt.savefig("orbital_period", dpi=100, bbox_inches='tight')
plt.close()

sns.boxplot(filtered_df['radius'])
plt.tight_layout()
plt.savefig("radius", dpi=100, bbox_inches='tight')
plt.close()

print("Create a excel file with the data")
filtered_df.to_excel('dataframe_output.xlsx', index=False)
