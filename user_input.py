import url_extraction_input as uei
import XGBoost_Classifier as xg
import re


import admin
if not admin.isUserAdmin():
        admin.runAsAdmin()

hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites=[]
url=input("Enter the URL : ")
url=input("Enter : ")
r=re.sub(r'^http[s]?://', '', url)
head, sep, tail = r.partition('/')

websites.append(head)


initial_output=uei.featureExtraction(url)
output=xg.input_data(initial_output)

if output==0:
    print("\n"+"Maximum Probability that it is a Legitimate Website")
else:
	print("\n"+"Maximum Probability that it is a Phishing Website")
	with open(hostsPath,'r+') as file:
		content=file.read()
		for site in websites:
			if site not in content:
				file.write(redirect+" "+site+"\n")
	

    