#!/usr/bin/env python
import feedparser
import os

def say(text):
	return os.system('echo {0} | festival --tts --language russian>/dev/null 2>&1'.format(text))

d = feedparser.parse('http://k.img.com.ua/rss/ru/all_news2.0.xml')
for entrie in d['entries']:
	print say(entrie['title'].encode('utf-8'))
