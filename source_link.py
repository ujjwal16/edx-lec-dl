import urllib2
import extract
def source(link):
	link=link.strip('\'"')
	log=open("log.txt",'a')	
	log.write("\n"+link)
	log.close()
	check=link.find("ht")
	if check==-1:
		link="http://"+link
	req=urllib2.Request(link)
	resp=urllib2.urlopen(req)
	content=resp.read()
	log1=open("log1.txt",'w')
	log1.write(content)
	list_url=[]
	position=0
	print "this is the active link " + link
	while True:
	 	link,position=extract.extract(content,position)
	 	
	 	
	 	if link!=None:
	 		pdf=link.find("pdf")
	 		if pdf == -1:
	 			list_url.append(link)
	 	else:
	 		break
	 	
	#print "\n".join(list_url)
	return list_url