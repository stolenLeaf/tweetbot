#importar dependencias
import tweepy
from memefier import memefy 


class MentionsListener(tweepy.StreamListener):

    def __init__(self,tweepy_wrapper):
        self.tweepy_wrapper = tweepy_wrapper
        self.api=tweepy_wrapper.api
        self.me=tweepy_wrapper.api.me()

    def on_status(self,tweet):
        print("se recibio el tweet con id", tweet.id)

        if tweet.in_reply_to_status_id!=None and tweet.user.screen_name!="tweetbot":
            #obtener tweet
            previous_tweet=self.tweepy_wrapper.get_tweet_by_id(tweet.in_reply_to_status_id)

        if previous_tweet.user.screen_name!="tweetbot":
            print(previous_tweet.text)

            #respodner tweet
            self.tweepy_wrapper.reply_to_tweet(tweet.user.screen_name,memefy(previous_tweet.text))
    def on_error(self,status):
        #mostrar error
        print("se detecto un error",status)