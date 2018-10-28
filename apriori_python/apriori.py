from collections import Counter
from itertools import chain, combinations

arr = []
minSupp = 2
noTransactions = (int)(raw_input("Enter the no of transactions : "))
conf = 75.0
items = []

for i in range(0,noTransactions) :
	items.append(list(raw_input("Enter the items pf transaction no "+str(i)+" with space between the items : ").split()))
		
print items

val = 1
itemSet = set()
for x in items :
	for xItem in x :
		itemSet.add(xItem)
LastL = []
LastLCount = []

while len(itemSet) >= val :
	LItems = []
	LItemCounts = []
	allC = list(combinations(itemSet,val))
	CItemSets = []

	itemSet = set()

	print "******************* C values ***************************"
	for j in range(0, len(allC)):
		CItemSets = list(allC[j])
		subItems = items
		for i in range(0, val) :
			subItems = [x for x in subItems if CItemSets[i] in x]
		print CItemSets, " \t: " , len(subItems)


		if len(subItems) >= minSupp :
			LItems.append(CItemSets)
			LItemCounts.append(len(subItems))
			for m in CItemSets :
				itemSet.add(m)

	print "***********************************************************\n\n"
	print itemSet

	if len(LItems) > 0 :
		LastL = LItems
		LastLCount = LItemCounts
		print "************************* L Items ***************************"
		for i in range(0, len(LItems)) :
			print LItems[i], "  \t: ",LItemCounts[i]
		print "***********************************************************\n\n"
		val = val+1

print "********************** FINAL L ********************************"
for i in range(0, len(LastL)) :
	print LastL[i], "  \t: ",LastLCount[i]
print "***********************************************************\n"

print "********************** CONF********************************"
val = val-1
ConfItems = []
ConfVal = []
for i in range(0, len(LastL)) :
	st = 1
	while st < val :
		supp = LastLCount[i]
		rhs = list(combinations(LastL[i],val-st))
		for j in rhs :
			lhs = list(combinations(set(LastL[i]).difference(set(j)),st))
			for k in lhs :
				confItems = items
				for valRhs in j :
					confItems = [x for x in confItems if valRhs in x]
				tempConf = 100 * supp/(float)(len(confItems))
				print j," => ",k, " \t : ", tempConf,"%"
				if tempConf >= conf :
					ConfItems.append(str(j)+" => "+str(k))
					ConfVal.append(tempConf)
		st = st+1
print "***********************************************************\n"

print "*********************FINAL CONF*************************\n"
for i in range(0, len(ConfVal)) :
	print ConfItems[i], "  \t: ",ConfVal[i]
print "***********************************************************\n"
