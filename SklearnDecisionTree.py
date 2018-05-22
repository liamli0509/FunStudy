# -*- coding: utf-8 -*-
"""
Created on Wed May 16 13:40:24 2018

@author: lil
"""

import pandas as pd
import os
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

os.chdir('U:/GitProject')

data = pd.read_csv('Iris.txt', sep=',')


X = data.values[:, 0:4]
Y = data.values[:, 4]

#split train and test using sklearn
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)


#Decision Tree Classifier with criterion gini index
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)
y_pred = clf_gini.predict(X_test)
print ("Accuracy is ", accuracy_score(y_test,y_pred)*100)
#Decision Tree Classifier with criterion information gain
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)
y_pred_en = clf_entropy.predict(X_test)
print ("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)


df = pd.DataFrame(y_test, columns=['test'])
df1 = pd.DataFrame(y_pred, columns=['prediction'])
df = pd.concat([df, df1], axis=1)


data[1].corr(data[3])
s1 = data[21].str.strip('CL').astype(int)
s2 = data[20].str.strip('CL').astype(int)
s1.corr(s2)