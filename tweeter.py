import tweepy
from authentication import *


def post(temperature, humidity):
    #authenticate with those credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    tweet = "At Vrilissia the temperature is " + temperature+" and the humidity is "+humidity
    api.update_status(tweet)
