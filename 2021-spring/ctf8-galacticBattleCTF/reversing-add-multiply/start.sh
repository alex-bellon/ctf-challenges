#!/bin/bash

while [ true ]; do
	su -l $USER -c "socat -dd TCP4-LISTEN:8008,fork,reuseaddr EXEC:'/build/$USER',pty,echo=0,rawer,iexten=0"
done;
