import pandas as pd
from importlib.resources import path
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from pathlib import Path
# from matplotlib import pyplot as plt
# data=pd.read_csv('final.csv')
p = Path(__file__).with_name('final.csv')
data=pd.read_csv(p)
y = data['Label']
y=np.array(y)

X = data.drop('Label',axis=1)
X=np.array(X)

def input_data(initial_output):
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.03)
    
    xgb = XGBClassifier(learning_rate=0.4,max_depth=7) 
    xgb.fit(X_train, y_train)

    y_test_predicted=xgb.predict(X_test)
    y_train_predicted=xgb.predict(X_train)

    acc_train_xgb = accuracy_score(y_train,y_train_predicted)
    acc_test_xgb = accuracy_score(y_test,y_test_predicted)

    print("XGBoost: Accuracy on training Data: {:.3f}".format(acc_train_xgb))
    print("XGBoost : Accuracy on test Data: {:.3f}".format(acc_test_xgb))

    url_vector=[initial_output]
    url_vector_np=np.array(url_vector)
    y_check_predict=xgb.predict(url_vector_np)
    return y_check_predict

# X=[]
# for i in range(len(X_test)):
#     X.append(i)

# plt.figure(figsize=(50,15))
# plt.plot(X,y_test_predicted,color="red",label="Predicted Value")
# plt.plot(X,y_test,color="blue",label="Actual Value")
# plt.title("XG Boost Classifier",fontsize=30)
# plt.xlabel("Cases",fontsize=25)
# plt.ylabel("Prediction",fontsize=25)
# leg = plt.legend(fontsize=25,loc=1)

# plt.show()





    








