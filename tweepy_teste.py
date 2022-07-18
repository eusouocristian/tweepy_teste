import tweepy

with open('token.txt') as f:
    for line in f:
        my_token = line

client = tweepy.Client(bearer_token=my_token)

# Replace with your own search query
query = '#Bolsonaro'

tweets = client.search_recent_tweets(query=query, tweet_fields=['text'], max_results=10)

for tweet in tweets.data:
   print(tweet.text)
