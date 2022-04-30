import GB_Classifier as gb
from feature import generate_data_set
import numpy as np

url=input("Enter : ")

x=np.array(generate_data_set(url)).reshape(1,30)

output=gb.input_data(x)

if output==1:
    print("Legit")
else:
    print("Phishing")