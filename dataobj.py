import pandas as pd
import numpy as np
from array import array

PRINT_DATA_DEBUG_MODE = True

# Read CSV
# From import XLSX import and then copy/paste from Excel into a file
df = pd.read_csv('geocyclab-datas.csv', header=[0], sep='\t')

# Match the "simple column name" (identifiant simplified name) with the real name (column name in the header CSV file)
mainFeatures = {'id': 'id', 'kms': 'kms', 'alti': 'alti', 'lat_deg': 'lat_deg', 'long_deg': 'long_deg', 'poids': 'Poids (g)', 'taille': 'taille'}

# All sorted objects
mainFeaturesSorted = {}

def prepare_sort_one_feature(feature):
    global df
    global mainFeatures
    #print(mainFeatures)

    if (feature not in mainFeatures):
        feature = 'id'

    result = df.sort_values(mainFeatures[feature], ascending=[1])

    return result

def prepare_all_sort():
    global mainFeaturesSorted
    global mainFeatures
    for featureId in mainFeatures.keys():
        mainFeaturesSorted[featureId] = prepare_sort_one_feature(featureId)

def getAllFeatures():
    global mainFeaturesSorted
    return mainFeaturesSorted.keys()


def getAllObjectsByFeature(feature):
    global mainFeatures
    #print(mainFeatures)

    if (feature not in mainFeaturesSorted):
        feature = 'id'

    return mainFeaturesSorted[feature]


print("Prepare all object sorted lists:")
prepare_all_sort()
print("Finish all sort:")

if PRINT_DATA_DEBUG_MODE:
    print("All available features:")
    print(getAllFeatures())

    for feature in mainFeatures:
        print("*********** BY " + feature)
        print(mainFeaturesSorted[feature])

