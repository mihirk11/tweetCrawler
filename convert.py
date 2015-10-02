# -*- coding: utf-8 -*-
import tweepy
import json
import codecs
from datetime import datetime
import pytz

d1={}
#with open("raw_tweets/20150917/entertainment.txt","r") as f:
#with open("raw_tweets/a.txt","r") as f:
with codecs.open("movie_ru.txt",'r', encoding='utf-8') as f:
	with codecs.open("movie_ru2.txt",'w', encoding='utf-8') as f2:
		for line in f:
			d=json.loads(line)
			d1["id"]=d["id"]
			d1["text_ru"]=d["text"]
			d1["lang"]=d["lang"]
			#print (d1["text_ru"])
			




			if d["entities"]["hashtags"]:
				hasht  = d["entities"]["hashtags"]
				List = []
				if not hasht:
					d1['tweet_hashtags'] = List
				else:
					for h in hasht:
						List.append(h['text'])
					d1['tweet_hashtags'] = List
					#print(d["entities"]["hashtags"][0]["text"])
					#d1["hashtags"]=d["entities"]["hashtags"][0]["text"]	

			if d["entities"]["urls"]:
				urls  = d["entities"]["urls"]
				uList = []
				if not urls:
					d1['tweet_urls'] = uList
				else:
					for u in urls:
						uList.append(u["expanded_url"])
					d1['tweet_urls'] = uList
					#print(d["entities"]["hashtags"][0]["text"])
					#d1["hashtags"]=d["entities"]["hashtags"][0]["text"]


			fmt = '%Y-%m-%dT%H:%M:%SZ'
			temp = datetime.strptime(d['created_at'],'%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=pytz.UTC)
			#print (temp.strftime(fmt))
			d1["created_at"]=temp.strftime(fmt)
			




			f2.write(json.dumps(d1,ensure_ascii=False))
			f2.write("\n")
			

 

en_secret = ''
