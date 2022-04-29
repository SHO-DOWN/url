import pandas as pd

df = pd.read_csv("final_dataset.csv")
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv('final.csv', index= False)

