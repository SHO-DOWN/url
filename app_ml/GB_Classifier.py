import numpy as np
import pandas as pd
from sklearn import metrics 
from sklearn.ensemble import GradientBoostingClassifier
from pathlib import Path
p = Path(__file__).with_name('dataset.csv')
data=pd.read_csv(p)
data = data.drop(['Index'],axis = 1)
X = data.drop(["class"],axis =1)
y = data["class"]

def input_data(initial_output):
    gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)
    gbc.fit(X,y)
    y_pred =gbc.predict(initial_output)[0]
    return y_pred


