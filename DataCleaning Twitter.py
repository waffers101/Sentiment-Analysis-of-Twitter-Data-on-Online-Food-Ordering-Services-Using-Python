
# coding: utf-8

# In[ ]:


#Code to import the data from the text file and then load it into an Array in Python.
#We use the json library because the data retrieved from Tweepy API is in the Java Script Object Notation Format.

import json
import os
tweets_data=[]

def dataclean(path,tweetarray):
    open('temp.txt','w')
    for line in open(path):
        if not line.isspace(): #stripping the data of the new lines before loading in the Array
            open('temp.txt','a').write(line) #creating a temp.txt which has the data without newlines 
        else:
            continue
    for line in open('temp.txt', 'r'):
        try:
            tweet=json.loads(line) #loading the json data into line by line into a string 
            tweetarray.append(tweet) #appending each string that contains the data for an individual tweet into the tweets Array
        except:
            continue
    os.remove('temp.txt')


# In[ ]:


dataclean('twitterdata6.txt', tweets_data) #passing the data files that were generated through the cleaning function 
dataclean('twitterdata7.txt', tweets_data)
dataclean('twitterdata9.txt', tweets_data)
dataclean('twitterdata10.txt', tweets_data)
dataclean('twitterdata11.txt', tweets_data)
dataclean('twitterdata12.txt', tweets_data)
dataclean('twitterdata13.txt', tweets_data)
dataclean('twitterdata14.txt', tweets_data)
dataclean('twitterdata15.txt', tweets_data)
dataclean('twitter_data4.txt', tweets_data)


# In[84]:


#extracting the text of the tweets from the entire data of the tweets to perform sentiment analysis.

count=0
tweets_text=[]
for tweet in tweets_data:
    if 'extended_tweet' in tweet:
        tweets_text.append(tweet['extended_tweet']['full_text'])
        count=count+1
    else:
        tweets_text.append(tweet['text'])
        count=count+1
print(count)

    


# In[94]:


#classification of tweets into tweets that are relevant for Zomato, Swiggy and FoodPanda Respectively.

zomato_tweets=[]
swiggy_tweets=[]
panda_tweets=[]
unclassified=[]
    
    
#function to check whether a particular word is present in the given tweet
def word_in_text(word, text):
    word=word.lower()
    text=text.lower()
    match=re.search(word, text)
    if(match):
        return 1
    else:
        return 0
    
#function for tweet classification which takes the array with the tweets as an argument             
           
def tweet_classification(textoftweets):
    for text in textoftweets:
        if word_in_text('zomato', text)==1:
            zomato_tweets.append(text)
        elif word_in_text('swiggy', text)==1:
            swiggy_tweets.append(text)
        elif word_in_text('foodpanda', text)==1:
            panda_tweets.append(text)
        else:
            unclassified.append(text)

tweet_classification(tweets_text)


# In[54]:



    
        


# In[55]:








# In[ ]:





# In[ ]:








# In[ ]:




