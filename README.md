# FunStudy
### Studynote while learning and playing with Python
This readme file contains the output and findings during Python/Spark learning and practice process, it is also the instruction file for codes in this project.

## KNN and Decision Tree
### Files related: KNN.py, SklearnDecisionTree.py, Iris.txt, drug.txt
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

## Monte Carlo for Option Pricing
## Binomial Tree for Option Pricing
## Using Spark/Pyspark to Estimate pi value
