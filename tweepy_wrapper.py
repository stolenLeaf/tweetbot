import tweepy
from tweepy import api

class TweepyWrapper:
    def __init__(self,consumer_key,consumer_secret,access_key,access_secret):
        #configura tweepy
        auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_key,access_secret)
        #almacenar referencia de API
        self.api=tweepy.API(auth)

    def get_tweet_by_id(self,tweet_id):
        #obtenemos un tweet por la id
        return self.api.get_status(tweet_id)

    def reply_to_tweet(self,username,tweet_id,text):
        #generar un Texto
        final_text='@{}"{}"'.format(username,text)
        self.api.update_status(final_text,in_reply_to_status_id=tweet_id)
