#!/bin/bash

idx=1
while read line; do
	#echo $line
	#echo $idx
	rtmpdump -r rtmp://flash.dce.harvard.edu/bounce -C B:0 -C Z: -C S:/$line -C S:BounceAPI3.0 -C N:0.000000 -C S:mp4 -y mp4:$line -o video$idx.mp4
	idx=$((idx + 1)) 
done < $1
