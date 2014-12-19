
def extract(content,postion):
	
	first=content.find("<a href",postion)
	if first == -1 :
		return None , 0
	else:
		second=content.find('http',first)
		third=content.find('"',second+1)
		#third=content.find('"',first)
		link=content[second:third]
		#link=content[first:third]
		#print link +"\n"
		#extract.counter+=1;
		#if extract.counter!=4:
		return link,third

	