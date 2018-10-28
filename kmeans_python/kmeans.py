import math, copy

noObjects = (int)(raw_input("Enter no of objects : "))
noAttr = 3
noClusters = 2

table = []
for i in range(0, noObjects) :
	table.append(list(raw_input("Enter the object no "+str(i)+" with spaces between attributes : ").split()))

ClusterCentres = [[1,1,2],[3,2,4]]
'''for i in range(0, noAttr) :
	ClusterCentres[i] = copy.copy(table[i])
'''

Clusters = [[],[]]
LastClusters = [[0,0,0],[0,0,0]]

while (not set(Clusters[0]) == set(LastClusters[0])) or (not set(Clusters[1]) == set(LastClusters[1])):
	LastClusters = copy.copy(Clusters)
	Clusters = [[],[]]
	for objectNo in range(0,len(table)) : 
		attrSet = copy.copy(table[objectNo])
		min = 999999
		closestClusterIndex = 0
		for i in range(0,noClusters) :
			x = abs((float)(ClusterCentres[i][0]) - (float)(attrSet[0]))
			y = abs((float)(ClusterCentres[i][1]) - (float)(attrSet[1]))
			z = abs((float)(ClusterCentres[i][2]) - (float)(attrSet[2]))
			dist = math.sqrt((x*x)+(y*y)+(z*z))
			if dist < min :
				min = dist
				closestClusterIndex = i
		
		Clusters[closestClusterIndex].append(objectNo)
	print Clusters

	for clusterIndex in range(0,noClusters) :
		sumx = 0.0
		sumy = 0.0
		sumz = 0.0
		for clusteredAttr in Clusters[clusterIndex]:
			sumx = sumx + (float)(table[clusteredAttr][0])
			sumy = sumy + (float)(table[clusteredAttr][1])
			sumz = sumz + (float)(table[clusteredAttr][2])
		ClusterCentres[clusterIndex][0] = sumx/(float)(len(Clusters[clusterIndex]))
		ClusterCentres[clusterIndex][1] = sumy/(float)(len(Clusters[clusterIndex]))
		ClusterCentres[clusterIndex][2] = sumy/(float)(len(Clusters[clusterIndex]))
	
	print "New Cluster Centres : ", ClusterCentres 

print "FINAL : ",LastClusters
