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
mainFeaturesSortedAscending = {}
mainFeaturesSortedDescending = {}

def prepare_sort_one_feature(feature, is_ascending):
    global df
    global mainFeatures
    #print(mainFeatures)

    if (feature not in mainFeatures):
        feature = 'id'

    isAscendingSort = 1
    if not is_ascending:
        isAscendingSort = 0

    result = df.sort_values(mainFeatures[feature], ascending=[isAscendingSort])
    return result

def prepare_all_sort():
    global mainFeaturesSorted
    global mainFeatures
    for featureId in mainFeatures.keys():
        mainFeaturesSortedAscending[featureId] = prepare_sort_one_feature(featureId, True)
        mainFeaturesSortedDescending[featureId] = prepare_sort_one_feature(featureId, False)

def getAllFeatures():
    global mainFeatures
    return mainFeatures.keys()


def getAllObjectsByFeature(feature, is_ascending):
    global mainFeatures
    #print(mainFeatures)

    if (feature not in mainFeatures):
        feature = 'id'

    if is_ascending:
        return mainFeaturesSortedAscending[feature]
    else:
        return mainFeaturesSortedDescending[feature]


print("Prepare all object sorted lists:")
prepare_all_sort()
print("Finish all sort:")

if PRINT_DATA_DEBUG_MODE:
    print("All available features:")
    print(getAllFeatures())

    for feature in mainFeatures:
        print("*********** (ASCENDING) BY " + feature)
        print(mainFeaturesSortedAscending[feature])
        print("*********** (DESCENDING) BY " + feature)
        print(mainFeaturesSortedDescending[feature])

