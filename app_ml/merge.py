import pandas as pd
df = pd.concat(
    map(pd.read_csv, ['phishing_dataset.csv','legit_dataset.csv']), ignore_index=True)

df = df.sample(frac=1).reset_index(drop=True)

df.to_csv('final_dataset.csv', index=False)




# merging two csv files
# df = pd.concat(
#     map(pd.read_csv, ['output1.csv','output2.csv','output3.csv','output4.csv','output5.csv','output6.csv','output7.csv','output8.csv','output9.csv','output10.csv','output11.csv','output12.csv','output13.csv','output14.csv','output15.csv','output16.csv',]), ignore_index=True)

# df.to_csv('legitimate_dataset.csv', index=False)

# df = pd.read_csv("phishing.csv")

# del df['Domain']
# df=df.fillna(0)
# del df['Unnamed: 18']
# del df['Unnamed: 19']
# del df['Unnamed: 20']

# df['Label']=df['Label'].replace(0,1)
# print(df)


# df.to_csv('phishing_dataset.csv', index=False)

