import pandas as pd

# Read the CSV file
df = pd.read_csv('sample_vaccine_with_toxicity.csv', low_memory=False)

print("Dataframe size:", len(df))

for i in range(0, len(df)):
    if df['toxicity'][i] >= 0.7:
        print(df['texts'][i] + "\n")
