#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author D4RKSH4D0WS
#Di kala gabut melanda...
try:
	import requests as r
	import os
except:
	os.system('pip2 install requests;python2 subdomain.py')
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
os.system('clear')
print '''
%s
╔═╗╦ ╦╔╗ ╔╦╗╔═╗  ╔═╗╦╔╗╔╔╦╗╔═╗╦═╗
╚═╗║ ║╠╩╗ ║║║ ║  ╠╣ ║║║║ ║║║╣ ╠╦╝
╚═╝╚═╝╚═╝═╩╝╚═╝  ╚  ╩╝╚╝═╩╝╚═╝╩╚═
%sPowered by https://indoxploit.or.id
'''%(G1,W1)
site=raw_input('%s╔═%s[ %sMasukkan website tanpa http/https %s]\n%s╚═%s[ %sInput %s]%s>%s '%(P1,G1,W1,G1,P1,G1,W1,G1,Y1,W1))
a=r.get('https://api.indoxploit.or.id/domain/'+site).json()
print
c=0
for w in a['data']['subdomains']:
	c+=1
	print '%s[%s%s%s] %s%s'%(P0,C0,c,P0,W0,w)
	open("hasil.txt","a+").write(w+"\n")
print
print '%s[%s>%s] %sHasil tersimpan di hasil.txt'%(G0,Y0,G0,W0)
