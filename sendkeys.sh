#!/bin/bash
while true
do
	/home/pi/hosampr/loop.py |  ssh auth@142.93.245.130 " cat>>/home/auth/rkeys.txt"
	date +%Y%m%d%H%M%S >> logs.txt
	sleep 6	
done