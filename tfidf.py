from collections import Counter
from math import sqrt, log


def printDoc(doc, label) :
	print "\n\n********************",label,"*************************"
	print "\t WORD \t\t TF \t\t IDF \t\t TF-IDF\t"
	for val in doc :
		print"\n"
		for key in val.keys():
			print "\t ",key,"\t\t ",val[key][2],"\t\t ",val[key][1],"\t\t ",val[key][0]
	print "***********************************************"

doc1List = Counter(list(open("doc1","r").read().split()))
doc2List = Counter(list(open("doc2","r").read().split()))
doc3List = Counter(list(open("doc3","r").read().split()))

docs = {}
table = []

noDocs = 3
doc1Sum = sum(doc1List.values())
doc2Sum = sum(doc2List.values())
doc3Sum = sum(doc3List.values())

for i in range(0,len(doc1List.keys())) :
	docs.update({doc1List.keys()[i] : (doc1List.values()[i] / (float) (doc1Sum))})
table.append(docs);
docs = {}
for i in range(0,len(doc2List.keys())) :
	docs.update({doc2List.keys()[i] : (doc2List.values()[i] / (float) (doc2Sum))})
table.append(docs);
docs = {}
for i in range(0,len(doc3List.keys())) :
	docs.update({doc3List.keys()[i] : (doc3List.values()[i] / (float) (doc3Sum))})
table.append(docs);

#printDoc(table,"TF")

for entries in table :
	for keys in entries.keys() :
		countDoc = len([x for x in table if keys in x.keys() ])
		idf = 1 + log(noDocs/(float)(countDoc))
		entries.update({keys : list([entries[keys] * idf, idf, entries[keys]])})

printDoc(table,"TF-IDF")

query = Counter(list(raw_input("Enter the query : ").split()))
querySum = sum(query.values())

docs = {}
for key in range(0, len(query.keys())) :
	docs.update({query.keys()[key] : (query.values()[key] / (float)(querySum))})

#printDoc(docs,"Query-TF")

for queryWord in docs.keys() :
		idf = list([x[queryWord] for x in table if queryWord in x.keys()])[0][1]
		docs.update({queryWord : [docs[queryWord] * idf, idf, docs[queryWord]]})

#printDoc(docs,"Query-TFIDF")

iterator = 0
for Documents in table :
	maxSimilarity = 0.0
	maxIndex = 0
	numerator = 0.0
	denDoc = 0.0
	denQ = 0.0
	for queryWord in query.keys() :
		denQ = denQ + (docs[queryWord][0] * docs[queryWord][0])
		if queryWord in Documents.keys() :
			numerator = numerator + (Documents[queryWord][0] * docs[queryWord][0])
			denDoc = denDoc + (Documents[queryWord][0] * Documents[queryWord][0])
	cosineSimilarity = numerator / (float)(sqrt(denDoc) * sqrt(denQ))
	print " \n\nCosineVal : ",cosineSimilarity
	if cosineSimilarity > maxSimilarity :
		maxSimilarity = cosineSimilarity
		maxIndex = iterator
	iterator = iterator + 1

print "\t The given query is closest to Document",iterator