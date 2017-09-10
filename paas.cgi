#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
cgitb.enable()
from random import randint

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

puser=data.getvalue('p')
a=randint(7777,9999)
if  puser == 'python':
	commands.getoutput('sudo docker run -itd -p '+str(a)+':4200 client')
	print  "plz wait for python launch !!"
	print  "<a href='https://192.168.2.20:"+str(a)+"'>"
	print   "click here for python"
	print   "</a>"

elif  puser == 'ruby':
	commands.getoutput('sudo docker run -itd -p '+str(a)+':4200 rubyclient')
	print  "wait for ruby "
	print  "<a href='https://192.168.2.20:"+str(a)+"'>"
	print   "click here for ruby"
	print   "</a>"

elif  puser == 'perl':
	commands.getoutput('sudo docker run -itd -p '+str(a)+':4200 perlclient')
	print  "perl is reloading "
	print  "<a href='https://192.168.2.20:"+str(a)+"'>"
	print   "click here for perl"
	print   "</a>"

	
else :
	print  "wrong choice !!"
	



