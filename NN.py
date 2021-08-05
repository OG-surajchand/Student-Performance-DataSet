# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:03:52 2021

@author: sctha
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
import tensorflow as tf
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from tensorflow import keras

#@ Import Data
Data_Set = pd.read_csv("student-por.csv",sep=";")

#@ Study Data
head = Data_Set.head()
Data_Set.info()
Data_Set.describe()

#@ Preprocessing
Data_Set.drop('school',axis=1,inplace=True)
Data_Set.drop('sex',axis=1,inplace=True)
Data_Set.drop('age',axis=1,inplace=True)
Data_Set.drop('address',axis=1,inplace=True)
Data_Set.drop('famsize',axis=1,inplace=True)
Data_Set.drop('Fedu',axis=1,inplace=True)
Data_Set.drop('Medu',axis=1,inplace=True)
Data_Set.drop('reason',axis=1,inplace=True)
Data_Set.drop('Mjob',axis=1,inplace=True)
Data_Set.drop('Fjob',axis=1,inplace=True)
Data_Set.drop('schoolsup',axis=1,inplace=True)
Data_Set.drop('famsup',axis=1,inplace=True)
Data_Set.drop('paid',axis=1,inplace=True)

LE = LabelEncoder()

Data_Set['Pstatus'] = LE.fit_transform(Data_Set['Pstatus'])
Data_Set['guardian'] = LE.fit_transform(Data_Set['guardian'])
Data_Set['activities'] = LE.fit_transform(Data_Set['activities'])
Data_Set['nursery'] = LE.fit_transform(Data_Set['nursery'])
Data_Set['higher'] = LE.fit_transform(Data_Set['higher'])
Data_Set['internet'] = LE.fit_transform(Data_Set['internet'])
Data_Set['romantic'] = LE.fit_transform(Data_Set['romantic'])

x = Data_Set.iloc[:,0:17].to_numpy(dtype="float")
y = Data_Set.iloc[:,17:20].to_numpy(dtype="float")

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,train_size=0.75,random_state=88)

#@ Linear Regression
model = LinearRegression()
model.fit(x_train,y_train)
y_predicted = model.predict(x_test)
accuracy_model1 = r2_score(y_test,y_predicted)

#@ Support Vector Machines
svr = SVR(epsilon=0.2)
model2 = MultiOutputRegressor(svr)

model2.fit(x_train,y_train)
y_predicted2 = model2.predict(x_test)

#@ Cross Evaluation
accuracy_model2 = cross_val_score(model2,y_test,y_predicted2,cv=5)    
mean_accuracy = accuracy_model2.mean()

#@ Artificial Neural Network
ANN = keras.models.Sequential()
ANN.add(keras.layers.Dense(34, input_dim=17, kernel_initializer='he_uniform', activation='relu'))
ANN.add(keras.layers.Dense(3))
ANN.compile(loss='mae', optimizer='adam')

ANN.compile(optimizer='adam', loss='mae',metrics=['Accuracy']) 

ANN.fit(x_train,y_train,batch_size=10,epochs=100)
y_predicted3 = ANN.predict(x_test)

#@ Getting and Predicting from User Data
print("Enter user data")
user = []
user.append(input("Pstatus: "))
user.append(input("guardian: "))
user.append(input("traveltime: "))
user.append(input("studytime: "))
user.append(input("failures: "))
user.append(input("activities: "))
user.append(input("nursery: "))
user.append(input("higher: "))
user.append(input("internet: "))
user.append(input("romantic: "))
user.append(input("famrel: "))
user.append(input("freetime: "))
user.append(input("go out: "))
user.append(input("Dalc: "))
user.append(input("Walc: "))
user.append(input("health: "))
user.append(input("absences: "))
df = pd.DataFrame(user).T
df = df.drop(0,axis=1)
df = df.to_numpy(dtype="float")
final_predictions = ANN.predict(df)

for column in final_predictions:
    print("Users grades are: ",final_predictions)
