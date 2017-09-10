#!/usr/bin/python 
import commands
commands.getstatusoutput('mkdir /media/qpo')
commands.getstatusoutput('mount 192.168.2.20:/server/qpo /media/qpo')
