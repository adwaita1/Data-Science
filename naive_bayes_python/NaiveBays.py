
#Assignment: To implement naive Bays classifier

import csv
import sys
import time
import os
from collections import Counter

file='datastr.csv'
f = open(file, 'rb')
query={'Age':'middle_age','Qualification':'MTech.','Experience':'medium','Work Type':'?'}
# you can also try to predict other attribute as follows
#query={'Age':'middle_age','Qualification':'?','Experience':'medium','Work Type':'Research'}


reader = csv.reader(f)
headers = reader.next()
#-----------------------------------------------
#declare datastructures
column = {}
freq = {}
Probability={}
occurance_counts={}
conditionaloccurance={}
condProb={}
FinalResults={}
Init_total=1.0
#-----------------------------------------------
#Function for calculating conditional probabilities:
def condProbfun(queryattribute_val,classlabel):
	value=0.0
	counter=0.0
	occure=0.0
	result=0.0
	f = open('datastr.csv', 'rb')
	reader = csv.reader(f)
	for row in reader:
		if queryattribute_val in row and classlabel in row:
			value= value+1
	occure=occurance_counts[classlabel]
	result=value/occure
	return result
#-----------------------------------------------
for h in headers:
	column[h] = []
for row in reader:
	for h, v in zip(headers, row):
		column[h].append(v)
print 'Display Dataset \n -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'
		
with open(file,'r') as f:
    for line in f:
        for word in line.split('\t'):
           print(word)
print '\n'
print '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*'
sys.stdin.read(1)
print 'Query tuple:',query

           
for h in headers:
	word_list = column[h]
	# Get a set of unique words from the list
	word_set = set(word_list)
	# create frequency dictionary
	
	for word in word_set:
	    occurance_counts[word]=word_list.count(word)  #Get occurance count
	    freq[word] = word_list.count(word) / float(len(word_list)) #Get frequency count
	    Probability[word]=freq[word] #prior probability
#-----------------------------------------------
for name,item in query.items(): #which class
        if item == '?':
                classname=name
               
print 'To Predict:',classname
print '-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n\n'
sys.stdin.read(1)
print 'Naive Bays Classifier.......\n'
time.sleep(5)
#-----------------------------------------------
word_list = column[classname]
word_set = set(word_list)

for word in word_set:
	classlabel=word # {Consultancy,Service,Research}
	print 'Prior probability of' ,classname,':',classlabel,'=',freq[classlabel]
	total=Init_total
	for queryattribute in query:
		if not queryattribute == classname:
			queryattribute_val=query[queryattribute] 
			#Get Every other attribute than classlabel print query[queryattribute]
			ans=condProbfun(queryattribute_val,classlabel)
			print '\n conditional probability  P(',queryattribute_val ,'|',classlabel,')=',ans
			total=total*ans
			condProb[classlabel]=total
	#print 'Total', total
			
	TotalProbability=total*freq[classlabel]	
	FinalResults[classlabel]=TotalProbability
	print '-----------------------------------------------'
	print 'Multiplication of above probabilities to give Posterior Probability of ',classname,':',classlabel,'=',FinalResults[classlabel]
	print '-----------------------------------------------\n\n\n\n\n\n'
	sys.stdin.read(1)
list=FinalResults.values()
#-----------------------------------------------
#Predict Classname
maxprob=max(list)
for name,item in FinalResults.items():
        if item == maxprob:
                classpredicted=name
print '*********************************************************'
print 'Predicted Class (Highest posterior Probability )for given query tuple is:',classname,':', classpredicted
print '*********************************************************'
#-----------------------------------------------

"""
OUTPUT:

student@siftworkstation:~/a5$ python NaiveBays.py
Display Dataset 
 -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Work Type,Age,Qualification,Experience

Consultancy,middle_age,Ph.D.,medium

Service,youth,MTech.,low

Research,youth,MTech.,low

Service,youth,BTech.,medium

Consultancy,middle_age,MTech.,high

Research,middle_age,Ph.D.,medium

Research,youth,BTech.,medium

Service,middle_age,MTech.,medium

Consultancy,senior,BTech.,high

Research,middle_age,Ph.D.,medium

-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
medium
Query tuple: {'Age': 'middle_age', 'Work Type': '?', 'Experience': 'medium', 'Qualification': 'MTech.'}
To Predict: Work Type
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

Naive Bays Classifier.......

Prior probability of Work Type : Service = 0.3

 conditional probability  P( middle_age | Service )= 0.333333333333

 conditional probability  P( medium | Service )= 0.666666666667

 conditional probability  P( MTech. | Service )= 0.666666666667
-----------------------------------------------
Multiplication of above probabilities to give Posterior Probability of  Work Type : Service = 0.0444444444444
-----------------------------------------------
Prior probability of Work Type : Consultancy = 0.3

 conditional probability  P( middle_age | Consultancy )= 0.666666666667

 conditional probability  P( medium | Consultancy )= 0.333333333333

 conditional probability  P( MTech. | Consultancy )= 0.333333333333
-----------------------------------------------
Multiplication of above probabilities to give Posterior Probability of  Work Type : Consultancy = 0.0222222222222
-----------------------------------------------

Prior probability of Work Type : Research = 0.4

 conditional probability  P( middle_age | Research )= 0.5

 conditional probability  P( medium | Research )= 0.75

 conditional probability  P( MTech. | Research )= 0.25
-----------------------------------------------
Multiplication of above probabilities to give Posterior Probability of  Work Type : Research = 0.0375
-----------------------------------------------

*********************************************************
Predicted Class (Highest posterior Probability )for given query tuple is: Work Type : Service
*********************************************************
student@siftworkstation:~/a5$ 

"""



























	





