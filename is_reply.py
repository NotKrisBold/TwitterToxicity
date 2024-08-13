import pandas as pd


df = pd.read_csv('sample_vaccine_with_toxicity.csv', low_memory=False)


df['hashtags'] = df['hashtags'].str.strip().str.replace(r'[\[\]\']', '', regex=True).str.split(",").apply(
    lambda x: ['#' + item.strip() for item in x] if isinstance(x, list) else x)

tweet_hashtags = pd.Series(df.hashtags.values, index=df.ids.astype(str)).to_dict()

# Filtrare i tweet di risposta
reply_tweets = df[df['is_reply'] == 'True']

# Verifica e stampa il risultato per ogni tweet di risposta
for idx, row in reply_tweets.iterrows():
    original_tweet_id = row['in_reply_to_id']

    if pd.notna(original_tweet_id):
        original_tweet_id_str = str(int(original_tweet_id))

        if original_tweet_id_str in tweet_hashtags:
            original_hashtags = tweet_hashtags[original_tweet_id_str]
            reply_hashtags = row['hashtags']

            if pd.isna(original_hashtags):
                print(f"Tweet ID {row['ids']}: False (original tweet has no hashtags)")
            elif pd.isna(reply_hashtags):
                print(f"Tweet ID {row['ids']}: False (reply tweet has no hashtags)")
            else:
                # Assicurarsi che entrambi gli hashtag siano liste
                if isinstance(original_hashtags, list) and isinstance(reply_hashtags, list):
                    # Controlla se ogni hashtag del tweet originale è presente nei tweet di risposta
                    all_hashtags_present = all(hashtag in reply_hashtags for hashtag in original_hashtags)

                    if all_hashtags_present:
                        print(f"Tweet ID {row['ids']}: True")
                    else:
                        print(f"Tweet ID {row['ids']}: False")
                else:
                    print(f"Tweet ID {row['ids']}: False (hashtags are not lists)")
        else:
            print(f"Tweet ID {row['ids']}: False (original tweet not found in tweet_hashtags dictionary)")
    else:
        print(f"Tweet ID {row['ids']}: False (original tweet not found or no in_reply_to_id)")
