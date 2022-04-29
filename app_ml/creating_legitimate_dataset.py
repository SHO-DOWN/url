import pandas as pd
import url_extraction as ue

data_l = pd.read_csv("legitimate_input.csv")
data_l.columns = ['URLs']
data_l.head()

# print(data_l)


legi_features = []
label = 0

for i in range(650,700):
  url = data_l['URLs'][i]
  legi_features.append(ue.featureExtraction(url,label))
  #print(legi_features)


feature_names = ['Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
                      'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic', 
                      'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards', 'Label']

legitimate = pd.DataFrame(legi_features, columns= feature_names)
legitimate.head()

legitimate.to_csv('output16.csv', index= False)

