import numpy
import pandas as pd
import numpy as np
import requests
import time

api_key_file_path = 'perspective_api.txt'

# Lettura chiave API
with open(api_key_file_path, 'r') as file:
    api_key = file.read().strip()

# Lettura dataframe
df = pd.read_csv('sample_vaccine_with_toxicity.csv', low_memory=False)

df['toxicity'] = np.nan
df.head(0).to_csv('sample_vaccine_with_toxicity_fix.csv', index=False)


# Funzione per mandare richiesta a Perspective API
def analyze_tweet_toxicity(tweet):
    url = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"
    params = {
        'key': api_key
    }
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'comment': {'text': tweet},
        'languages': ['it'],
        'requestedAttributes': {'TOXICITY': {}}
    }

    response = requests.post(url, headers=headers, params=params, json=data)
    if response.status_code == 200:
        result = response.json()
        return result['attributeScores']['TOXICITY']['summaryScore']['value']
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


for i in range(len(df)):
    if type(df['toxicity'][i]) is not numpy.float64:
        print(i)
        print(type(df['toxicity'][i]))
        #df.loc[i, 'toxicity'] = analyze_tweet_toxicity(df.loc[i, 'texts'])
    df.iloc[[i]].to_csv('sample_vaccine_with_toxicity_fix.csv', mode='a', header=False, index=False)
    #time.sleep(1)
