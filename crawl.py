from sys import argv
import source_link
from merge import merge
script ,link =argv
#source_link.source(link)
first_visit=[link]
visited=[]
log2=open("visited.txt",'w')
while first_visit:
	active=first_visit.pop()
	if active not in visited:
		link_list=source_link.source(active)
		visited.append(active)
		first_visit=merge(first_visit,link_list)
		print "===================================="
		print "merged list "+"\n".join(first_visit)
		print "===================================="
			
		log2.write("\n"+active)
		
log2.close()
print visited




