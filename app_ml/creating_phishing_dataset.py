import pandas as pd
import url_extraction as ue


data_p=pd.read_csv("phishing_input.csv")
# phishurl = data_p.sample(n = 6, random_state = 2).copy()
# phishurl = phishurl.reset_index(drop=True)
# phishurl.head()

phish_features=[]
label=1
for i in range(500,600):
    url=data_p['url'][i]
    phish_features.append(ue.featureExtraction(url,label))
    print(phish_features)

feature_names = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
                      'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 
                      'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards', 'Label']

phishing = pd.DataFrame(phish_features, columns= feature_names)
phishing.head()

phishing.to_csv('phishing_output1.csv', index= False)

# print(new_df)

