from sys import argv
import urllib2
import extract
script ,link =argv
req=urllib2.Request(link)
resp=urllib2.urlopen(req)
content=resp.read()
extract.extract.counter=0
extract.extract(content,0)