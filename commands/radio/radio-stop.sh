#!/bin/bash
ps ax|grep 'SCREEN -S radio -d -m mplayer'|awk {'print $1'}|xargs -i{} kill -9 {}
