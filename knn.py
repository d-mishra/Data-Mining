# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 13:59:36 2015

@author: DM
"""
import csv
import random
#x=0
#y=0
## import the dataset
#with open('C:/data/R/mydata/bezdekIris.data','rb') as csvfile:
#    lines=csv.reader(csvfile)
#    for rows in lines:
#        print ','.join(rows) #join concatenates a sequence of strings using a separator


#Fucntion to read file and Split dataset to training set and test set
def loadDataSet (filename,split,trainingSet=[],testSet=[]):
    with open(filename,'rb') as csvfile:
        lines=csv.reader(csvfile)
        for rows in lines:
#            print ','.join(rows) #join concatenates a sequence of strings using a separator
            dataset=list(lines)
# Split dataset to training set and test set
            for x in range(len(dataset)-1):
                for y in range(4):
                    dataset[x][y] = float(dataset[x][y])
                if random.random()<split:
                    trainingSet.append(dataset[x])
                else:
                    testSet.append(dataset[x])
                
## Test the function                
#trainingSet=[]
#testSet=[]
#loadDataSet('C:/data/R/mydata/bezdekIris.data',0.7,trainingSet,testSet)
#print "Training Set " + repr(len(trainingSet))            

#calculating Eucledian Distance

import math
def eucledianDistance (instance1,instance2,length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)
    
## TEst Eucledian distance function
#instance1=[1,4,10,'a']
#instance2=[23,3,32,'b']
#
#eucledianDistance(instance1,instance2,3)

#Finding the k most nearest neighbors
import operator
def getNeighbors(trainingSet,testInstance,k):
    distances=[]
    length=len(testInstance)-1
    for x in range(len(trainingSet)):
        dist=eucledianDistance (testInstance,trainingSet[x],length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


##test getNeighbors fucntion  
#trainingSet=[[1,4,2,'a'],[4,2,6,'d']]
#testInstance=[4,4,4]
#k=1
#neighbors=getNeighbors(trainingSet,testInstance,1)  

#Prediction of attribut
import operator
def getResponse(neighbors):
    classVotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response]=1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

#test getRespnse    
neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = getResponse(neighbors)
print response


#Test Accuracy
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] is predictions[x]:
              correct += 1
	return (correct/float(len(testSet))) * 100.0
 

testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print(accuracy)

def main():
# Prepare Data
    trainingSet=[]
    testSet=[]
    split = .70
    loadDataSet('C:/data/R/mydata/bezdekIris.data',split,trainingSet,testSet)
    print 'Train set: ' + repr(len(trainingSet))
    print 'Test set: ' + repr(len(testSet))
    
# Predictions
    predictions=[]
    k=3
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
	
main()



















