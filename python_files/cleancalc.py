import pandas as pd
import numpy as np
import matplotlib as plt
import zipfile
import sys
from pandas import ExcelWriter
import re
from pandas import ExcelFile
print("Starting check...")
data = pd.read_excel('datasets/MASTER_DATASET.xlsx')
print("Datafile opened, now checking...")
total_count = len(data)
for column in data.columns:
    items = data[column]
    count = items.isnull().sum()
    percentage = (count / total_count) * 100
    print(column, "=", percentage)
