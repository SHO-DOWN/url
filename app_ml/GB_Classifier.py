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
    y_legit = gbc.predict_proba(initial_output)[0,1]
    return y_pred,y_legit


# import pandas as pd
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# # from matplotlib import pyplot as plt 
# from pathlib import Path
# p = Path(__file__).with_name('dataset.csv')
# data=pd.read_csv(p)
# data = data.drop(['Index'],axis = 1)
# X = data.drop(["class"],axis =1)
# y = data["class"]

# X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 42)
    
# gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7) 
# gbc.fit(X_train, y_train)

# y_test_predicted=gbc.predict(X_test)
# y_train_predicted=gbc.predict(X_train)

# acc_train_gbc = accuracy_score(y_train,y_train_predicted)
# acc_test_gbc = accuracy_score(y_test,y_test_predicted)

# print("Gradient Boosting Classifier : Accuracy on training Data: {:.3f}".format(acc_train_gbc))
# print("Gradient Boosting Classifier : Accuracy on test Data: {:.3f}".format(acc_test_gbc))

# def input_data(initial_output):
#     gbc = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)
#     gbc.fit(X,y)
#     y_pred =gbc.predict(initial_output)[0]
#     y_phishing = gbc.predict_proba(initial_output)[0,0]
#     y_legit = gbc.predict_proba(initial_output)[0,1]
#     return y_pred,y_legit

# print("The URL is {0:.2f} % safe to go.".format(legit*100))

