#!/bin/bash

while [ true ]; do
	su -l $USER -c "socat -dd TCP4-LISTEN:9000,fork,reuseaddr EXEC:'/usr/bin/python3 -u /ev.py',pty,echo=0,raw,iexten=0"
done;
