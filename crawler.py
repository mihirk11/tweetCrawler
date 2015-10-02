# -*- coding: utf-8 -*-
import tweepy
import json
import codecs

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
auth.set_access_token(access_token, access_token_secret)
 
 
 
api = tweepy.API(auth)
#f =open ("книги.txt","a")


i=0 
query="фильм since:2015-09-15 until:2015-09-16"
with codecs.open('movie_ru.txt','w', encoding='utf-8') as f:
	for r in tweepy.Cursor(api.search,q=query,count=100, lang="ru").items():
		j=json.dumps(r._json,ensure_ascii=False)
		j2=""
		j2=j
		j1=json.loads(j)
	#	f.write(r._json["id_str"])
		#f.write(j2.encode('utf-8'))
		f.write(j2)
		i=i+1
		if i>300:
			break		
		f.write("\n")
			
# for tweets in tweepy.Cursor(api.search, q=query,lang='en', count=100).pages(10):
	# print (tweets[0].text)