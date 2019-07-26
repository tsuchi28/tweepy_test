import tweepy
import tauth

api = tauth.api

mozi = 'HelloWorld' #ツイート内容

api.update_status(mozi + "\ntweepy") 
print('Done!')