#!/usr/bin/env python
import feedparser
import os
import sys


def say(text, lang='english'):
    if lang=='russian': 
	os.system('echo \'{0}\' | festival --tts --language russian>/dev/null 2>&1'.format(text))
    else:
        os.system('espeak \'{0}\'>/dev/null 2>&1'.format(text))

def main(argv):
    lang=argv[0]
    text=argv[1] 
    say(text, lang)

if __name__ == "__main__":
    if len(sys.argv)>=2:
        main(sys.argv[1:])
    else:
        print "It needs arguments"
