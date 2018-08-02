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

functions:
```python
login():#log in to Indeed.ca
searcher(keyword, city):#Search job and location
list_job():#get job titles/id on the webpage to a list
scorer(goodWords, badWords, textString):#search job summary and assign a score
match(input_list):#get job title, job score and job url
```

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
|4|Senior Analyst, Planning & Optimization - Programmatic job - Omnicom Media Group - Toronto, ON|www.indeed.ca/viewjob?jk=4e476397b1d291fa|
|3|Analyst, Customer Insights job - The Home Depot - Toronto, ON |www.indeed.ca/viewjob?jk=65eb7047fb436e93|




## Monte Carlo for Option Pricing
### Code: MonteCarloEUCall.py [Code](https://github.com/liamli0509/FunStudy/blob/master/MonteCarloEUCall.py)
Using Monte Carlo to estimate option price

## Binomial Tree for Option Pricing
### Code: Binomial_Tree.py [Code](https://github.com/liamli0509/FunStudy/blob/master/Binomial_Tree.py)
Using Binomial Tree to estimated option price (Amercian Option has no closed solution)

## Using Spark/Pyspark to Estimate pi value
First try on Spark. Spark is probably the better tool if we deal with large amount of data. Spark has different APIs and 

