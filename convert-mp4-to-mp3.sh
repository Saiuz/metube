#!/bin/bash
# Note: requires ffmpeg
# https://askubuntu.com/a/174300

set -e

for f in $1/*.mp4
do
    name=`echo "$f" | sed -e "s/.mp4$//g"`
    ffmpeg -i "$f" -vn -ar 44100 -ac 2 -ab 192k -f mp3 "$name.mp3"
    rm "$name.mp4"
done
