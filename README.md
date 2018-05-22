# FunStudy
### Studynote while learning and playing with Python
This readme file contains the output and findings during Python/Spark learning and practice process, it is also the instruction file for codes in this project.

## KNN and Decision Tree
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

## Monte Carlo for Option Pricing
## Binomial Tree for Option Pricing
## Using Spark/Pyspark to Estimate pi value
