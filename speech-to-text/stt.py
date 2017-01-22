#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import subprocess
import os

DIR='/opt/intelligent-house'
DIC_DIR="/opt/intelligent-house/speech-to-text/dic"
DIC_NUMBER=3634
HI='HI HOUSE'

COMMAND_EXEC="""/usr/local/bin/pocketsphinx_continuous \
            -lm {0}/{1}.lm \
            -dict {0}/{1}.dic \
            -keyphrase "{2}" \
            -kws_threshold 1e-20 \
            -inmic yes \
            -logfn /dev/null 2>/dev/null""".format(DIC_DIR, DIC_NUMBER, HI)

def runProcess(exe):
    p = subprocess.Popen(exe, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        retcode = p.poll() #returns None while subprocess is running
        line = p.stdout.readline().strip()
        if not line in  ['\n', '\r\n'] and len(line)>1: yield line
        if(retcode is not None):
            break

def getDir(command):
    return os.path.join(DIR, command)

for line in runProcess(COMMAND_EXEC):
    print "Voice command: {}".format(line)
    if line == "RADIO PLAY":
        print "execute RADIO PLAY"
        os.system(getDir("commands/radio/radio-play.sh http://icecast.radiohitfm.cdnvideo.ru/hit.mp3"))
    elif line == "RADIO STOP":
        print "execute RADIO STOP"
        os.system(getDir("commands/radio/radio-stop.sh"))
    elif line == "DECREASE VOLUME":
        os.system("amixer set 'Speaker' 20%-")
    elif line == "INCREASE VOLUME":
                os.system("amixer set 'Speaker' 20%+")
    elif line in ["HI HOUSE", "HI"]:
        print "execute HI HOUSE"
        os.system(getDir("commands/say/say.py") + " 'english' 'Hello my master'")
