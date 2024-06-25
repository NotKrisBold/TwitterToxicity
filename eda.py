import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lettura dataframe
df = pd.read_csv('sample_vaccine.csv', low_memory=False)

print(df.head())

"""# Rielaborazione dei dati"""

df.loc[~df['is_reply'].isin(['True', 'False']), 'is_reply'] = np.nan
print("is_reply:", df['is_reply'].unique())

"""# Informazioni generali"""

print(df.info())

"""Quantità di valori nulli per colonna"""

print(df.isnull().sum())

colors = ['skyblue', 'lightgreen']

original_count = df['is_original'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(original_count, labels=original_count.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribuzione tweet originali', fontsize=16)
plt.axis('equal')
plt.show()

quoted_count = df['is_quoted'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(quoted_count, labels=quoted_count.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribuzione tweet quoted', fontsize=16)
plt.axis('equal')
plt.show()

reply_count = df['is_reply'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(reply_count, labels=reply_count.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribuzione tweet di risposta', fontsize=16)
plt.axis('equal')
plt.show()

retweet_count = df['is_retweet'].value_counts()
retweet_count = retweet_count.reindex([False, True], fill_value=0)
plt.figure(figsize=(8, 8))
plt.pie(retweet_count, labels=retweet_count.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribuzione retweet', fontsize=16)
plt.axis('equal')
plt.show()

"""# Analisi tossicità"""