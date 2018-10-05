#! /usr/bin/python
import subprocess
import os
import time
import base64

results = subprocess.check_output(['iwlist','wlan0','scan'])
dd=[s.strip() for s in results.splitlines()]
k=1
m=1
n=1
l=1
for i in dd:
    if "10:DA:43:C2:09:19" in i:
        m=k
    if "9C:3D:CF:0B:BB:F3" in i:
        n=k
    if "A0:04:60:75:D8:7E" in i:
        l=k
    k=k+1

#Assigning keys
if m==1:
    key1="000000"
    pkey1="000"
else:
    key1=dd[m+4]
    key1=key1[11:31]
    key1=key1.decode('base64')
    key1=int(key1)/766776
    key1=str(key1).zfill(6)    
	
    pkey1=dd[m+2]
    pkey1=pkey1[28:31]
if n==1:
    key2="0000000"
    pkey2="000"
else:

    key2=dd[n+4]
    key2=key2[11:31]
    key2=key2.decode('base64')
    key2=int(key2)/766776
    key2=str(key2).zfill(6) 
    pkey2=dd[n+2]
    pkey2=pkey2[28:31]
if l==1:
    key3="000000"
    pkey3="000"
else:

    key3=dd[l+4]
    key3=key3[11:31]
    key3=key3.decode('base64')
    key3=int(key3)/766776
    key3=str(key3).zfill(6) 
    pkey3=dd[l+2]
    pkey3=pkey3[28:31]

#printing
print ""
print ">",(time.strftime("%H:%M:%S")),key1+"*"+pkey1+"**"+key2+"*"+pkey2+"**"+key3+"*"+pkey3
