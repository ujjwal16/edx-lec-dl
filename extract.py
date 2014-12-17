
def extract(content,postion):
	
	first=content.find("<a href",postion)
	if first == -1 :
		return None , 0
	else:
		second=content.find('"',first)
		third=content.find('"',second+1)
		link=content[second+1:third]
		#print link +"\n"
		#extract.counter+=1;
		#if extract.counter!=4:
		return link,third

	