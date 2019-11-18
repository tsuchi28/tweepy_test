import tweepy
import tauth

api = tauth.api

text = 'HelloWorld' #ツイート内容

api.update_status(text + "\ntweepy") 
print('Done!')
