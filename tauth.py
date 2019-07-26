#coding:UTF-8
import tweepy

CONSUMER_KEY = ""          #入力
CONSUMER_SECRET = ""       #入力

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

ACCESS_TOKEN = ""          #入力
ACCESS_TOKEN_SECRET = ""   #入力

print("auth")
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
print("Done!")