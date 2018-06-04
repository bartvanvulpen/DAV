import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data
data = pd.read_csv("stage3.csv")

# function to delete column if more than 40% of the values is unknowm
total_count = len(data)
for column in data.columns:
    items = data[column]
    count = items.isnull().sum()  
    percentage = (count / total_count) * 100
    print(column, "=", percentage)
    if percentage >= 40.0:
        data = data.drop(column, 1)
