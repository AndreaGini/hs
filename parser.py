#!/usr/bin/python

import urllib2

separator = '<-->'
remotelog='http://c.hlp.sc/ZKtU/download/test-sample.log'
try:
    logread=urllib2.urlopen(remotelog)
    for line in logread:
        if '<=' in line:
            msgid = line.split(' ')
            topic = line.partition('T=')
            print 'Message ID:',msgid[3],separator,'Message Topic:',topic[2]

except urllib2.HTTPError, e:
        print 'URL Failed with error code - %s.' % e.code
