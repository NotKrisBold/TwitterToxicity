import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lettura file csv
df = pd.read_csv('sample_vaccine_with_toxicity.csv', low_memory=False)

# print(df.info())

# Correzzione dati colonna is_reply
df['is_reply'] = df['is_reply'].apply(lambda x: x if x in [True, False] else np.nan)
print("is_reply:", df['is_reply'].unique())

# Conversione hashtags in list
df['hashtags'] = df['hashtags'].str.strip().str.replace(r'[\[\]\']', '', regex=True).str.split(",").apply(
    lambda x: ['#' + item.strip() for item in x] if isinstance(x, list) else x)
print("Dataframe size:", len(df))

# Conversione della colonna 'created_at' in datetime
df['created_at'] = pd.to_datetime(df['created_at']).dt.tz_localize(None)

# ANALISI TOSSICITÀ MEDIA PER MESE
df['year_month'] = df['created_at'].dt.to_period('M')
mean_toxicity_per_month = df.groupby('year_month')['toxicity'].mean().reset_index()
mean_toxicity_per_month['year_month'] = mean_toxicity_per_month['year_month'].dt.to_timestamp()

plt.figure(figsize=(12, 6))
plt.plot(mean_toxicity_per_month['year_month'], mean_toxicity_per_month['toxicity'], marker='o')
plt.title('Media della Tossicità per Mese')
plt.xlabel('Mese')
plt.ylabel('Media della Tossicità')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ANALISI DISTRIBUZIONE TOSSICITÀ
plt.figure(figsize=(10, 6))
plt.hist(df['toxicity'], bins=30, edgecolor='black')
plt.title('Distribuzione della Tossicità')
plt.xlabel('Tossicità')
plt.ylabel('Frequenza')
plt.grid(True)
plt.tight_layout()
plt.show()

# TOSSICITÀ IN BASE ALL'ORARIO DEL GIORNO
df['hour'] = df['created_at'].dt.hour
mean_toxicity_per_hour = df.groupby('hour')['toxicity'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(mean_toxicity_per_hour['hour'], mean_toxicity_per_hour['toxicity'], marker='o')
plt.title('Media della Tossicità per Orario del Giorno')
plt.xlabel('Ora del Giorno')
plt.ylabel('Media della Tossicità')
plt.grid(True)
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# HASHTAG PIÙ TOSSICI
# TODO DA RIGUARDARE
df_exploded = df.dropna(subset=['hashtags']).explode('hashtags')
hashtag_toxicity = df_exploded.groupby('hashtags')['toxicity'].mean()
toxic_hashtags = hashtag_toxicity[hashtag_toxicity > 0.1]
df_filtered = df_exploded[df_exploded['hashtags'].isin(toxic_hashtags.index)]
hashtag_counts = df_filtered['hashtags'].value_counts()
top_10_hashtags = hashtag_counts.head(5)

plt.figure(figsize=(15, 8))
top_10_hashtags.plot(kind='barh', color='skyblue')
plt.xlabel('Frequenza')
plt.ylabel('Hashtag')
plt.title('Top 5 hashtag più tossici e popolari')
plt.gca().invert_yaxis()
plt.show()

# TOSSICITÀ NEL TEMPO NEGLI HASHTAG PIÙ USATI
df_exploded = df.dropna(subset=['hashtags']).explode('hashtags')
top_hashtags_list = df_exploded['hashtags'].value_counts().head(10).index.tolist()
df_top_hashtags = df_exploded[df_exploded['hashtags'].isin(top_hashtags_list)]

df_top_hashtags.loc[:, 'year_month'] = df_top_hashtags['created_at'].dt.to_period('M')

mean_toxicity_per_month_hashtag = df_top_hashtags.groupby(['year_month', 'hashtags'])['toxicity'].mean().reset_index()
mean_toxicity_per_month_hashtag['year_month'] = mean_toxicity_per_month_hashtag['year_month'].dt.to_timestamp()

plt.figure(figsize=(14, 8))
for hashtag in top_hashtags_list:
    hashtag_data = mean_toxicity_per_month_hashtag[mean_toxicity_per_month_hashtag['hashtags'] == hashtag]
    plt.plot(hashtag_data['year_month'], hashtag_data['toxicity'], marker='o', label=hashtag)
plt.title('Andamento della Tossicità nei 10 Hashtag più Popolari')
plt.xlabel('Mese')
plt.ylabel('Media della Tossicità')
plt.legend(title='Hashtag', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
