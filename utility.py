import urllib2 
import os,sys
import re
import pafy
def merge(list1,list2):

    if not list1:
       return list2

    elif not list2:
       return list1
    else:
        list1=list(set(list1)|set(list2))
        return list1
  

def download(link_list,file_name):
  os.chdir(file_name)
  for link in link_list:
    if (".pdf" or ".doc" or ".zip" or ".mp3") in link:
      req=urllib2.Request(link)

      try:
        usock = urllib2.urlopen(req) 
      except urllib2.HTTPError, e:
        print e.code
        continue
      except urllib2.URLError, e:
        print e.args
        continue                         
      
      file_name =link.split('/')[-1]                                
      f = open(file_name, 'wb')                                     
      #file_size = int(usock.info().getheaders("Content-Length")[0]) 
      print "Downloading: %s " % (file_name)#, file_size)

      downloaded = 0
      block_size = 8192     
      while True:                                     
       buff = usock.read(block_size)
       if not buff:
        break
       
       downloaded = downloaded + len(buff)
       f.write(buff)
       #download_status = r"%3.2f%%" % (downloaded * 100.00 / file_size) 
       #download_status = download_status + (len(download_status)+1) * chr(8)
      f.close()
      print "done"#download_status,"done"
    else:
      print "following link is not downloadable-> %s"%link  
  
def form_list(search):
  return re.sub("[^\w]"," ",search).split()
def strict_list(visited,search_list):
  strict=[]
  
  for link in visited:
    flag=0
    for word in search_list:
      if word.lower() in link.lower():
        flag=1
        continue
      else:
        falg=0
        break
    if flag==1:
       strict.append(link)
  return strict 

def lenient_list(visited,search_list):
  lenient=[]
  for link in visited:
    if any(word.lower() in link.lower() for word in search_list):
      lenient.append(link)
  return lenient     
#=======================================
def download_video(dfile):
    choice=raw_input("1. Want best quality for all videos\n2. Choose quality for each video\nEnter : ") 
    path=raw_input("Enter path to directory : ")

    show=bool(raw_input("Press 1 to hide downloading status or Press Enter to show : "))
    
    for l in dfile:
        video=pafy.new(l)
        print "\n",video.title
        if choice=='1':
            best = video.getbest(preftype="mp4")
            print video.title," downloading..."
            filename=best.download(filepath=path,quiet=show)
        if choice=='2':
            i=0
            for stream in video.streams:
                print i,".)",stream
                i=i+1;
            stream_quality=raw_input("Enter required quality(Serial no.) : ")
            stream_quality=int(stream_quality)
            print video.title,"downloading..."
            filename=video.streams[stream_quality].download(filepath=path,quiet=show)
        print "\n",video.title,"Done"
         
    return
def vid_id(link_list):
    vid=[]
    for link in link_list:
      req=urllib2.Request(link)
      resp=urllib2.urlopen(req)
      print "status_code=>%d" %resp.getcode()
      content=resp.read()
      vid=vid+re.findall(r'data-streams=&#34;(?:0.75:.{11},)?1.00?:(.{11})',content)
      #print "\n".join(vid)
    return vid  

