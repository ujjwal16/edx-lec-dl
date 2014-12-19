import urllib2
import extract
from bs4 import BeautifulSoup
def source(link,seed):
	#link=link.strip('\'"')
	print "=************************************************entered source******************************************** \n"
	list_url=[]
	log=open("log.txt",'a')	
	log.write("\n"+link)
	log.close()
	# check=link.find("ht")
	# if check==-1:
	# 	link="http://"+link
	print "this is the active link--> " + link
	req=urllib2.Request(link)
	try:
		resp=urllib2.urlopen(req)
	except urllib2.HTTPError, e:
    		print e.code
    		return list_url
	except urllib2.URLError, e:
    		print e.args
    		return list_url
	#resp=urllib2.urlopen(link)
	content=BeautifulSoup(resp)
	
	position=0
	a_list=content.find_all('a')
	if not a_list:
		return list_url
	else:
		for link in a_list:
			x=link.get('href')
			if x is not None:
				print "========================================================="+x
				#x=x.encode('ascii')
				if x :
					if x.find("htt")==-1:
						x=seed+x[x.find("/"):]
					#if x[0]!='#':
					list_url.append(x)
		print list_url
		return list_url
 # 	while True:
	#  	link,position=extract.extract(content,position)
	#  	if link!=None and "\\" not in link:
	#  		pdf=link.find("pdf")
	#  		if pdf == -1:
	#  			list_url.append(link)
	#  	else:
	#  		break
	 	
	# #print "\n".join(list_url)
	# return list_url