#encoding=utf-8
import sys
import requests


f = open(sys.argv[1], "r",encoding="utf-8")
#print(f.read())
concatenated_lines = ""
lines=f.readlines()
for line in lines:
	concatenated_lines = concatenated_lines + line
concatenated_lines = concatenated_lines +"\n"
#print(concatenated_lines)

loginURL = 'http://120.126.151.132/'

headers = {'User-Agent': 'ntpu-rbtn-user',}
formdata = {'raw_text':concatenated_lines}
session = requests.Session()
 
response=session.post(loginURL ,data = formdata)

#goto_URL = 'http://120.126.151.132/cgi-bin/RBTN.cgi'
#response = session.get(goto_URL, headers = headers)
 
response.encoding="utf-8"

key_start_line="<textarea rows=\"14\" cols=\"50\">"
key_end_line="</textarea>"

#print (response.text)
flag=0
lines=response.text.splitlines()
for i in range(len(lines)):
	now=lines[i].strip()
	if(now==key_end_line):
		break
	if(flag==1 and (lines[i]!='' or lines[i+1]!=key_end_line)):
		print(lines[i])
	if(now[:30]==key_start_line[:30]):
		print(now[30:])
		flag=1
	
