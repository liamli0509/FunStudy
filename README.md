# FunStudy
### Studynote while learning and playing with Python
This readme file contains the output and findings during Python/Spark learning and practice process, it is also the instruction file for codes in this project.

## Rank Jobs on Indeed base on keywords
### Code: [Code](https://github.com/liamli0509/FunStudy/blob/master/Indeed_Find_Me_Jobs.py)

Craw Indeed job search results and rank them by keywords in job summary/description.

Logic:
1. Login to Indeed.ca
2. Enter job title and location
3. Sort by date
4. Grab all information(title, job description, URL) of each job
5. Search keywords in job description, add one point for 'good' keywords and deduce one point for 'bad' keywords
6. Put all info into a dataframe (sort by scores high to low) and write to a excel file

Example:
Search for Quantitative Jobs in Toronto, ON, take jobs first two pages, match with 'good' and 'bad' keywords and assign scores.

```python
good = ['Python','data', 'SQL', 'investment', 'travel', 'AWS', 'quantitative', 'analytical', 'master', 'MSc',\
        'modelling']
bad = ['5+', 'C++', 'sales', 'CPA', 'Java']
main('Quantitative', 'Toronto, ON', 2)
```

Sample output:

|Job Score|Job Title|Job URL|
| --- | --- | --- |
|5|Intern - Quantitative Analyst, Risk Model Validation (4 month contract) job - Ontario Teachers' Pension Plan - Toronto, ON |www.indeed.ca/viewjob?jk=8cd96a69143f042a|
|5|Analyst, BI & Reporting job - Thinking Capital - Toronto, ON|www.indeed.ca/viewjob?jk=8a9f215327782141|
|5|Data Scientist job - ChefHero - Toronto, ON |www.indeed.ca/viewjob?jk=1b5d6d63675d8f3a|


## KNN and Decision Tree
### Code and Data: KNN.py, SklearnDecisionTree.py, Iris.txt, drug.txt [Code](https://github.com/liamli0509/FunStudy/blob/master/KNN.py), [Code](https://github.com/liamli0509/FunStudy/blob/master/SklearnDecisionTree.py)
KNN and Decision Tree are two famous and classic Machine Learning algorithms to classify data base on different features. KNN stands for K-Nearest-Neighbors and it works as following.
For every point in our dataset:
1.	calculate the distance between dataset and the current point
2.	sort the distances in increasing order
3.	take k items with lowest distances to dataset
4.	find the majority class among these items (vote among the nearest K)
5.	return the majority class as the prediction for the class of dataset
The KNN algorithm works well with numeric data and does not require assumptions about data. However, it requires large amount of computing, especially when the data has large number of features.

Decision Tree is another algorithm to classify the data, it requires less computing in general. But we must make assumptions first and pick which features are used to split the data. Decision Tree is easier to understand the learning result and can deal with irrelevant features. It usually works as following:
1.	make a first decision on the dataset to dictate which feature is used to split the data
2.	To determine this, you try every feature and measure which split will give you the best results. 
3.	The subsets will then traverse down the branches of the first decision node. If the
data on the branches is the same class, then you’ve properly classified it and don’t need
to continue splitting it.
4.	If the data isn’t the same, then you need to repeat the splitting process on this subset. The decision on how to split this subset is done the same way as the original dataset, and you repeat this process until you’ve classified all the data.


Let's first play withe the famous Iris data (Iris.txt), which is classify Iris (kind of flower) base on 4 numeric features.
KNN.py and SklearnDecisionTree.py contains the code to generate the following result.

Let's plot the data first and we can cleanly see the flowers are well classified as the gaps between different groups are large.

```python
import seaborn as sns
sns.pairplot(plotData, hue = "Class", palette='husl')
```

![Image of Iris](https://github.com/liamli0509/FunStudy/blob/master/IrisPlot1.png)

Then apply KNN, split the train and test set by 70% and 30% and vote among the nearest 3 (K=3):
```python
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
```
The output is
```
Train set: 109
Test set: 41
Accuracy: 90.2439024390244% when k=3
```
If we increase K to 4:
```
Train set: 104
Test set: 46
Accuracy: 93.47826086956522% when k=4
```
And K to 6:
```
Train set: 103
Test set: 47
Accuracy: 97.87234042553192% when k=6
```
It turns out K=6 give the best prediction, however, higher K value does not always lead to better prediction and it requires more computing.

On the other hand, I used the DecisonTreeClassifier from sklearn to build the decision tree, sklearn is a Python module which has multi machine learning algorthms within it.
If we do the following:
```python
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100, max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)
y_pred_en = clf_entropy.predict(X_test)
print ("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)
```
The output is
```
Accuracy is  93.3333333333
```

## Monte Carlo for Option Pricing
### Code: MonteCarloEUCall.py [Code](https://github.com/liamli0509/FunStudy/blob/master/MonteCarloEUCall.py)
Using Monte Carlo to estimate option price

## Binomial Tree for Option Pricing
### Code: Binomial_Tree.py [Code](https://github.com/liamli0509/FunStudy/blob/master/Binomial_Tree.py)
Using Binomial Tree to estimated option price (Amercian Option has no closed solution)

## Using Spark/Pyspark to Estimate pi value
First try on Spark. Spark is probably the better tool if we deal with large amount of data. Spark has different APIs and 

