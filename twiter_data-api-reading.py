import tweepy

import json

# Lire les clés d'API depuis le fichier secrets.txt
with open('C:\\Users\\dell\\Desktop\\Kafka_Tp\\TwiterKafkaTp\\secrets.txt') as f:
    for line in f:
        if '=' in line:
            key, value = line.strip().split(" = ")
            if key == 'CONSUMER_KEY':
                CONSUMER_KEY = value.strip("'")
            elif key == 'CONSUMER_SECRET':
                CONSUMER_SECRET = value.strip("'")
            elif key == 'ACCESS_TOKEN':
                ACCESS_TOKEN = value.strip("'")
            elif key == 'ACCESS_TOKEN_SECRET':
                ACCESS_TOKEN_SECRET = value.strip("'")

# Authentification avec Tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
cursor= tweepy.Cursor(api.search_tweets, q='music', lang="en", tweet_mode='extended').items(50)

for tweet in cursor:
    hashtags = tweet.entities['hashtags']
    hashtext = list()
    for j in range(0, len(hashtags)):
        hashtext.append(hashtags[j]['text'])
    
cur_data = {
    "id_str": tweet.id_str,
    "username": tweet.user.name,
    "tweet": tweet.full_text,
    "location": tweet.user.location,
    "created_at": tweet.created_at.isoformat(),
    "retweet_count": tweet.retweet_count,
    "favorite_count": tweet.favorite_count,
    "followers_count": tweet.user.followers_count,
    "lang": tweet.lang,
    "coordinates": tweet.coordinates
}
print(cur_data)