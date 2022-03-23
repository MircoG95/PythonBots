
#https://developer.twitter.com/en
#Importieren des Moduls tweepy in Konsole: py -m pip install tweepy

import tweepy
import time



# API Key, API Key Secret

auth = tweepy.OAuthHandler("APIKEY","APIKEYSECRET")

# Access Token, Access Token Secret

auth.set_access_token("ACCESSTOKEN","ACCESSTOKENSECRET")



api = tweepy.API(auth, wait_on_rate_limit=True)



# Nach nrTweets suchen die das Suchwort enthalten

search = '#wurst'

nrTweets = 100



# Liken der gefundenen Tweets

for tweet in tweepy.Cursor(api.search_tweets,search).items(nrTweets):

    try:

        print('Tweet Liked')

        tweet.favorite()

        time.sleep(10)

    except tweepy.TweepyException as e:

        print(e.args)



# Statusupdate

# api.update_status("Dies ist ein Test.")
