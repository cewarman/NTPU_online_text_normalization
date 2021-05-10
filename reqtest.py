#encoding=utf-8
import sys
import requests


f = open(sys.argv[1], "r",encoding="utf-8")
#print(f.read())
concatenated_lines = ""
lines=f.readlines()
for line in lines:
	concatenated_lines = concatenated_lines + line
concatenated_lines = concatenated_lines +"\n       "

loginURL = 'http://120.126.151.132/cgi-bin/RBTN.cgi'

headers = {'User-Agent': 'ntpu-rbtn-user',}
formdata = {'myTag':concatenated_lines}
session = requests.Session()
 
response=session.post(loginURL ,data = formdata)
 
#goto_URL = 'http://120.126.151.132/cgi-bin/RBTN.cgi'
#response = session.get(goto_URL, headers = headers)
 
response.encoding="utf-8"

key_start_line="</textarea>                    <textarea rows=\"9\" name=\"myTag\" cols=\"58\">"
key_end_line="</textarea>                    <br>"

#print (response.text)
flag=0
lines=response.text.splitlines()
for i in range(len(lines)):
	if(lines[i]==key_end_line):
		break
	if(flag==1 and lines[i + 1] != key_end_line):
		print(lines[i])
	if(lines[i]==key_start_line):
		flag=1
