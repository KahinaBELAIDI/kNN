#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv

with open('iris.data.txt', 'r') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines :
        print (', '.join(row))

#Next we need to split the data into a training dataset 


# # Handle Data

# In[16]:


import csv
import random
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
                if random.random() < split:
                    trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])


# # knn with euclidian distance

# In[17]:



import math

def euclideanDistance(data1, data2, length):
    sum = 0
    for i in range(int(length)):
        sum += pow((data2[i]-data1[i]),2)
    distance = math.sqrt(sum)
    return distance


# In[18]:


import operator

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])

    return neighbors


# In[19]:


import operator

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][ -1 ] 
        if response in classVotes:
            classVotes[response] +=1
        else:
            classVotes[response] =1 
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)

    return sortedVotes[0][0]


# In[20]:


def getAccuracy(testSet, predictions):
    correct=0
    for i in range(len(testSet)):
        if testSet[i][-1]==predictions[i]:
            correct+=1
    return round((correct/float(len(testSet))) * 100.0,2)


# # apply knn to iris dataset

# In[22]:


trainingSet=[]

testSet=[]

loadDataset('iris.data.txt', 0.66, trainingSet, testSet)

print ('Train: ' + repr(len(trainingSet)))

print ('Test: ' + repr(len(testSet)) )


# In[25]:


neighbors = []
for test in testSet:
    neighbors.append(getNeighbors(trainingSet, test, 3))


# In[24]:


responses=[]
for i in range(len(neighbors)):
    responses.append(getResponse(neighbors[i]))
accuracy = getAccuracy(testSet, responses)
print(accuracy,"%")

