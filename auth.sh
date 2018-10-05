#!/bin/bash
read -p "Username>" username
echo $username
nohup /home/pi/hosampr/sendkeys.sh &>/dev/null &
echo -ne "Sending APs information"
for i in 1 2 3 4 5 6 7
do
   echo -ne "."
   sleep 1
done

ssh $username@142.93.245.130
ps -ef | grep sendkeys.sh | grep -v grep | awk '{print $2}' | xargs kill

