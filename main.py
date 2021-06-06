#importar dependencias
import tweepy
from tweepy_wrapper import tweepy_wrapper
from mentions_listener import mentions_listener
from credenciales import credentials

# crear instancia de la clase tweetwrapper
tweepy_wrapper=tweepy_wrapper(credentials['CONSUMER_KEY'],credentials['CONSUMER_SECRET'],credentials['ACCESS_KEY'],credentials['ACCESS_SECRET'])
#escuchar menciones
mentions_listener=mentions_listener(tweepy_wrapper)
stream=tweepy.Stream(tweepy_wrapper.api.auth,mentions_listener)
stream.filter(track=['@tweetbot'])