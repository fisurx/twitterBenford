import os 
import tweepy

CONSUMER_KEY = os.environ.get("API_KEY")
CONSUMER_SECRET_KEY = os.environ.get("API_KEY_S")

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET_TOKEN = os.environ.get("ACCESS_TOKEN_S")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

api = tweepy.API(auth)

api.update_status("bot working")