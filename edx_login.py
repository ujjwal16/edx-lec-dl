import urllib,urllib2, cookielib,json
from bs4 import BeautifulSoup
from datetime import timedelta, datetime
from sys import argv
#==========================================================# website information
home= 'https://www.edx.org'
login_page = 'https://courses.edx.org/login'
dashboard = 'https://www.edx.org/dashboard'
login_app=login_page + "_ajax"
script ,user_email,user_pswd=argv
#===========================================================
print user_email
print user_pswd
print login_app
#===========================================================#for getting response header and cookie information

c = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
urllib2.install_opener(opener)
response = urllib2.urlopen(login_page)
set_cookie = {}
for cookie in c:
	set_cookie[cookie.name] = cookie.value

#===========================================================# preparing header

headers = {'User-Agent': 'edX-downloader/0.01',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
'Referer': "https://courses.edx.org",
'X-Requested-With': 'XMLHttpRequest',
'X-CSRFToken': set_cookie.get('csrftoken', '') }
csrf=headers['X-CSRFToken']
print "csrf token" +csrf
#===========================================================# creating login data
post_data = urllib.urlencode({
'email' : user_email,
'password' : user_pswd,
'remember':False
}).encode('utf-8')
print post_data
#===========================================================#sending request to login_app ,Method=POST
request = urllib2.Request(login_app, post_data,headers)
response = urllib2.urlopen(request)
print "repsonse code=%d" %response.getcode()
data=response.read().decode('utf-8')
resp=json.loads(data)
#===========================================================# to check the login 
print data

if not resp.get('success',False):
	print "error"
else:
	print "success"

#==========================================================#redirecting to dasboard
req = urllib2.Request(dashboard)
resp = urllib2.urlopen(req)
print resp.getcode()
print resp.read().find("ujjwal16")
