# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:54:54 2018

@author: lil
"""

import pandas as pd
import os
import math
import random
import operator
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir('U:/GitProject')


############################################################
#Read Iris data
############################################################
data = pd.read_csv('Iris.txt', sep=',', header=None)
#correlation = data.corr()


#############################################################
#Plot the data before start KNN
#############################################################
plotData = pd.read_csv('Iris.txt', sep=',', header=None)
plotData.columns = ['SL', 'SW', 'PL', 'PW', 'Class']
plt.figure()
#sns.pairplot(plotData, hue = "Class", size=3)
sns.pairplot(plotData, hue = "Class", palette='husl', kind='reg')
plt.show()


##########################################################
#Normallize function 1 (if needed)
##########################################################
def Normallization(dataset):
    from sklearn.preprocessing import normalize
    norData = normalize(dataset, norm='max')
    return(norData)


############################################################
#Normallize 2 (if needed)
##########################################################
#NormData = (data-data.min())/(data.max()-data.min())
#NormData = pd.DataFrame(NormData)  
#############################################################


############################################################
#Define number of columns as a global variable, make sure the class to predict is the last columns
ncol = len(data.columns)  
##############################################################



##################################################################
#Split training and test datasets in a random way
#################################################################
def splitData(dataset, ratio):
    trainingSet = pd.DataFrame()
    testSet = pd.DataFrame()
    for i in range(len(dataset)):
        if random.random() < ratio:
            trainingSet = trainingSet.append(dataset.iloc[i])
        else:
            testSet = testSet.append(dataset.iloc[i])
    return(trainingSet, testSet)


#####################################################################
#Computing the distance between two records
####################################################################
def Distance(row1, row2):
    distance = sum(pow(row1[0:(ncol-1)]-row2[0:(ncol-1)], 2))
    return math.sqrt(distance)

#####################################################################
#Get nearest k-neighbors
######################################################################
def Neighbors(trainingSet, testInstance, k):
	distances = []
	for i in range(len(trainingSet)):
		dist = Distance(testInstance, trainingSet.iloc[i])
		distances.append((trainingSet.iloc[i], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = pd.DataFrame()
	for i in range(k):
		neighbors = neighbors.append(distances[i][0])
	return neighbors

##################################################################
#Vote on the nearest K and get prediction
#####################################################################
def Response(neighbors):
	classVotes = {}
	for i in range(len(neighbors)):
		response = neighbors.iloc[i,-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

#####################################################################
#Accurat percentage check
#####################################################################
def getAccuracy(testSet, predictions):
	correct = 0
	for i in range(len(testSet)):
		if testSet.iloc[i,-1] == predictions[i]:
			correct += 1
	return (correct/len(testSet)) * 100.0

#run main function
def main():
	train, test = splitData(data, 0.7)
	print ('Train set: ' + repr(len(train)))
	print ('Test set: ' + repr(len(test)))
	predictions=[]
	k = 3
	for i in range(len(test)):
		neighbors = Neighbors(train, test.iloc[i], k)
		result = Response(neighbors)
		predictions.append(result)
	accuracy = getAccuracy(test, predictions)
	print('Accuracy: ' + repr(accuracy) + '% when k=' + repr(k))
	
main()


