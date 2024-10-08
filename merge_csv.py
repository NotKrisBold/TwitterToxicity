import pandas as pd
from urllib.parse import urlparse
import numpy as np

file1 = 'sample_vaccine_with_toxicity.csv'
file2 = 'news-guard.csv'

df1 = pd.read_csv(file1, low_memory=False)
df2 = pd.read_csv(file2, encoding='latin1', low_memory=False)

df1['urls'] = df1['urls'].str.strip().str.replace(r'[\[\]\']', '', regex=True).str.split(",").apply(
    lambda x: [item.strip() for item in x] if isinstance(x, list) else x)


# Funzione per estrarre il dominio
def extract_domain(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        return domain[4:] if domain.startswith('www.') else domain
    except Exception as e:
        print(f"Errore nell'estrazione del dominio: {e}")
        return np.nan


df1_expanded = df1.explode('urls')
df1_expanded['Domain'] = df1_expanded['urls'].apply(
    lambda url: extract_domain(url) if isinstance(url, str) else np.nan)

df1.rename(columns={'urls': 'url'}, inplace=True)

# Merge
merged_df = pd.merge(df1_expanded, df2, on='Domain', how='left')

# Salvataggio
merged_df.to_csv('merged_1.csv', index=False)

print("DataFrame finale salvato in 'merged.csv'")
