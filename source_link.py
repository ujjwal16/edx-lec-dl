import urllib2
import extract
def source(link):
	req=urllib2.Request(link)
	resp=urllib2.urlopen(req)
	content=resp.read()
	list_url=[]
	position=0

	while True:
	 	link,position=extract.extract(content,position)
	 	if link!=None:
	 		list_url.append(link)
	 	else:
	 		break
	 	
	print "\n".join(list_url)