# -*- coding: utf-8 -*-
"""Breast Cancer Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E63UpbCsOPKvyzIvgyd3m1ouSfymZLgI
"""

# Breast Cancer Detection using Logistic Regression

import numpy as np
import sklearn.datasets as skd

# getting the datasets
breast_cancer = skd.load_breast_cancer()
print(breast_cancer)

X= breast_cancer.data
Y= breast_cancer.target
print(X)
print(Y)

print(X.shape, Y.shape)

# import data in Pandas data frame
import pandas as pd

data = pd.DataFrame(breast_cancer.data, columns = breast_cancer.feature_names)
data['Class'] = breast_cancer.target
data.head()

data.describe()

print(data['Class'].value_counts())

print(breast_cancer.target_names)

data.groupby('Class').mean()

"""0 - Malignant
1 - Benign

Train and test split
"""

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test = train_test_split(X,Y)

print(Y.shape,Y_train.shape,Y_test.shape)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.1)
# test_size --> to specify the percentage of test data needed

print(Y.shape,Y_train.shape,Y_test.shape)

print(Y.mean(),Y_train.mean(),Y_test.mean())

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.1, stratify = Y)
# stratify --> for correct distribution of data as of the original data

print(Y.mean(),Y_train.mean(),Y_test.mean())

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.1, stratify = Y, random_state = 1)
# random_state --> Specific split of data, each value of random_state splits the data differently

print(X_train)

"""**Logistic Regression**"""

# import Logistic Regression from sklearn
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression() # loading the logistic regression model to the variable 'classifier'

# training the model on training data
classifier.fit(X_train,Y_train)

"""Evaluation of the model"""

# import accuracy_score
from sklearn.metrics import accuracy_score

prediction_on_training_data = classifier.predict(X_train)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)

print('Accuracy_on_training_data is:',accuracy_on_training_data)

# prediction on test data
prediction_on_test_data = classifier.predict(X_test)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)

print('Accuracy_on_test_data is:',accuracy_on_test_data)

"""Detecting  whether the patient has breast cancer in benign or Malignant stage"""

input_data = (17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189)
# change the input_data to numpy_array to make prediction
input_data_as_numpy_array = np.asarray(input_data)
print(input_data)

#reshape the array as we are predicting the output for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# prediction
prediction = classifier.predict(input_data_reshaped)
print(prediction) # returns a list with element [0] if Malignant; returns a listwith element [1], if Benign

if(prediction == 0):
  print('The breast cancer is Malignant')
else:
  print('The breast cancer is Benign')