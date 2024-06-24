import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sample_vaccine.csv', low_memory=False)

print(df.head())

# Informazioni generali
print(df.info())

# Statistiche descrittive
print(df.describe())

