import tweepy

my_token = 'AAAAAAAAAAAAAAAAAAAAAFm%2BewEAAAAA7tWlQNChQ1Yon%2BR9iExWk978yB8%3D0wtLeLiVo3f1LNKxxegAyr3He8sAiGjPuRU2wzusobb8sPGL6X'

client = tweepy.Client(bearer_token=my_token)

# Replace with your own search query
query = '#Bolsonaro'

tweets = client.search_recent_tweets(query=query, tweet_fields=['text'], max_results=10)

for tweet in tweets.data:
   print(tweet.text)
