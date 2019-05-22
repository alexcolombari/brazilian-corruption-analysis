from __future__ import absolute_import, division, print_function

import pathlib

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

file_name = 'dataset.xlsx'
df = pd.read_excel(file_name, sheet_name = 1)

'''dfs = {sheet_name: xl_file.parse(sheet_name) 
          for sheet_name in xl_file.sheet_names}'''

# Drop columns with NaN values
df = df.drop(df.columns[[3, 4, 5, 6]], axis=1)

# Filter DF data with only target name
filtered_data = df[df["Target"] == 'DEM']
total = df['Type'].sum()
print("Total: {}".format(total))

