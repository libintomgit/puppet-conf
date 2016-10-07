#! /usr/bin/python
import sys
import os
import subprocess

arg=(sys.argv)
 #arg1=(sys.argv)[1] (cannot provide this, since this will revert with error if no argv is provided)

if len(arg)==2:
	if (arg)[1].endswith('.corp.inmobi.com'):
		print "hostname is correct.\nProceeding with the further proceedures"
		p = subprocess.Popen(["fping", (arg)[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		stdout, stderr = p.communicate()
		if 'alive' in stdout.split():
			print "SSHing to %s server " % arg[1]
		a= stderr
	else:
			print (arg)[1], "is not a proper corp hostname <*.corp.inmobi.com>"
else:
	print "Please provide the proper hostname after this script <puppet_config_corp_server.py> <*.corp.inmobi.com>  "



