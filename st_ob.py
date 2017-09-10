#!/usr/bin/python2

import  cgi,cgitb
import  commands,time

cgitb.enable()

print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
d_name=x.getvalue('d')
d_size=x.getvalue('s')

print  "<pre>"
print  commands.getoutput('sudo  lvcreate  --name '+d_name+'  --size '+d_size+'M  cloudvg')
print  commands.getoutput('sudo mkfs.xfs  -f  /dev/cloudvg/'+d_name)
print  commands.getoutput('sudo mkdir -p /server/'+d_name)
print  commands.getoutput('sudo mount  /dev/cloudvg/'+d_name+'  /server/'+d_name)
print  commands.getoutput('sudo echo "/server/'+d_name+' *(rw,no_root_squash)" >/etc/exports')
print  commands.getoutput('sudo exportfs -r')
print  "</pre>"

print  "successfully Done"
##########ClientSide###########
commands.getstatusoutput("sudo touch client.py")
commands.getstatusoutput("sudo chmod 777 client.py")
f=open('client.py','w')
f.write('#!/usr/bin/python \n')
f.write('import commands\n')
f.write("commands.getstatusoutput('mkdir /media/"+d_name+"')\n")
f.write("commands.getstatusoutput('mount 192.168.2.20:/server/"+d_name+" /media/"+d_name+"')\n")
f.close()

commands.getstatusoutput("sudo tar -cvf client.tar client.py")
commands.getstatusoutput("sudo cp -rvf client.tar /var/www/html/")

time.sleep(4)

print   "<META HTTP-EQUIV=refresh CONTENT='0 ; URL=http://192.168.2.20/client.tar\n'>"





