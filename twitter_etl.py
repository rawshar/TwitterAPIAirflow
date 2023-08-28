import tweepy
import pandas as pd
import json
from datetime import datetime


def run_twitter_et():

    access_key = ""
    access_secret = ""
    consumer_key = ""
    consumer_secret = ""

    # Twitter authentication

    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    # Creating an api object
    api = tweepy.API(auth)

    # screen_name is used to get a particular user
    # count get the number of tweets, 200 is max
    # rts means retweets so we kept it as False
    #
    tweets = api.user_timeline(screen_name='@elonmusk', count=200, include_rts = False, tweet_mode = 'extended')

    # check the above code is working
    # print(tweets)
    # we get the JSON data so need transformation

    tweet_list = []

    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text': text,
                        'favorite_count': tweet.favorite_count,
                        'retweet_count': tweet.retweet_count,
                        'created_at': tweet.created_at}

        tweet_list.append(tweet_list)

    df = pd.DataFrame(tweet_list)
    df.to_csv("elonmusk_twitter_data.csv")
