# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import matplotlib as plt

data = pd.read_csv("data.csv")
df = pd.DataFrame(data)


print(df.head())