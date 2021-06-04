#Streaming the relevant Tweets from Twitter using the Twitter API for Python called Tweepy.

import tweepy
import io
import json
import pprint

#the consumer_key, access_token etc are generated from twitter.developer.com after registering an App for the project.
consumer_key='Your consumer_key'
consumer_secret='Your consumer_secret'
access_token='Your access_token'
access_secret='Your access_secret'

#tweepy uses the OAuthHandler method to connect to Twitter API.
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

#We are using the Streaming method of Tweepy to Stream tweets in real time from Twitter.
class MyStreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("We are connected to the Twitter server.")
        pass

    def on_data(self, raw_data):  #overriding the on_data method of StreamListener class to capture the data from Tweets.
        print(raw_data) #prints the raw data that is then stored into a text file 
        return True
     
    def on_error(self, status):
        print(status)

    def on_timeout(self, notice):
        print("The connection has timed out:"+notice)
        return True
    
    def on_disconnect(self, notice):
        print(notice)
        return True 

    
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener, tweet_mode='extended',retry_time_start=5.0)
#use of retry_time_start attriute of the Stream object is important inorder to refresh the connection to the Twitter server otherwise the request times out. 
myStream.filter(track=['swiggy','zomato','foodpanda'])
#the Filter method is used inorder to filter the relevant tweets by a set of keywords so that our stream only picks up the tweets that have these keywords in them. 

