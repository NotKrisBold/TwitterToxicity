import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('merged.csv', encoding='latin1', low_memory=False)

print(df.head())

print(df.describe())

print(df.info())

#print(df['Domain'][1], df['Parent Domain'][1])
