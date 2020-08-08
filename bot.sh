#!/bin/bash

# send a bot to background with:
#
# $ setsid ./bot.sh

tail -f -n 1 /home/infection/.local/share/teeworlds/dumps/infcroya.txt | ./piper.py 1>>bot.log 2>> bot.error
