import pandas as pd
import numpy as np
import requests
import time

api_key_file_path = 'perspective_api.txt'

# Open the file and read the API key
with open(api_key_file_path, 'r') as file:
    api_key = file.read().strip()

# Read the CSV file
df = pd.read_csv('sample_vaccine.csv', low_memory=False)

# Initialize the toxicity column
df['toxicity'] = np.nan

# Save the header of the DataFrame
df.head(0).to_csv('sample_vaccine_with_toxicity.csv', index=False)


# Function to send request to Perspective API
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


# Loop through the DataFrame and analyze toxicity
for i in range(len(df)):
    df.loc[i, 'toxicity'] = analyze_tweet_toxicity(df.loc[i, 'texts'])
    df.iloc[[i]].to_csv('sample_vaccine_with_toxicity.csv', mode='a', header=False, index=False)
    print(i)
    time.sleep(1)
