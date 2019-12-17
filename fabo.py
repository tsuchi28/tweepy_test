#coding:UTF-8
import tweepy
import tauth
import sys
api = tauth.api
print('検索ワードを入力してください:')
q = input()    #検索するキーワード
print('ツイート数を入力してください：')
count = int(input())    #表示させるツイート数
search_res = api.search(q = q,count = count)
for res in search_res:
	user_id = res.id
	print(user_id)    #ツイートIDの表示
	username = res.user.name
	print(username)    #アカウント名の表示
	tweet = res.text
	print(tweet)    #ツイートの表示
	try:
		api.create_favorite(user_id)    #ふぁぼる
		sys.stdout.write(username)
		print("をふぁぼりました")
	except:    #既にふぁぼってる時に実行
		pass
	print("------------------")    #区分け線
print("Done!")
