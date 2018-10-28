from collections import Counter

table = []
entry ={}
query = {}
noEntries = (int)(raw_input("Enter no of entries : "))

noAttributes = (int)(raw_input("Enter no of attributes : "))
Attr = list(raw_input("Enter all Attribues : ").split())
	
for i in range(0,noEntries) :
	print "Enter entry no ",(i+1)," : "
	entry = {}
	for j in range(0,noAttributes) :
		entry.update({Attr[j] : raw_input("\t Enter the value for "+str(Attr[j])+" : ")})
	table.append(entry)

print "Enter query : "
for j in range(0,noAttributes-1) :
	query.update({raw_input("\t Enter attribute name : ") : raw_input("\t Enter the value : ")})
	
label = list(set(Attr) - set(query.keys()))[0]

distinctSet = set([attr[label] for attr in table])
distinctVal = Counter([attr[label] for attr in table])
print " Counter ",distinctVal

maxProb = 0
assignedLabel = ""
for classLabel in distinctSet :
	prob = 1.0
	for i in query.keys() :
		#l = Counter([attr[i] for attr in table])
		prob = prob * len([attr[i] for attr in table if (attr[label]==classLabel) and (attr[i] == query[i])]) / (float)(distinctVal[classLabel])

	prob = prob * distinctVal[classLabel] / (float)(noEntries)
	print classLabel, " : ", prob
	if prob > maxProb :
		assignedLabel = classLabel
		maxProb = prob

print " Assigned Class Label : ",assignedLabel