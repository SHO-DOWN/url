import time
from datetime import datetime as dt
import re
import admin
if not admin.isUserAdmin():
        admin.runAsAdmin()

hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites=[]
url=input("Enter : ")
r=re.sub(r'^http[s]?://', '', url)
head, sep, tail = r.partition('/')

websites.append(head)
# websites = ["makautexam.net","freemovies2021.com"]
# print(websites)

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,10):
		print ("Sorry Not Allowed...")
		with open(hostsPath,'r+') as file:
			content=file.read()
			for site in websites:
				if site not in content:
					file.write(redirect+" "+site+"\n")
					
	else:
		with open(hostsPath,'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(site in line for site in websites):
					file.write(line)
			file.truncate()
		print ("Allowed access!")
	time.sleep(5)