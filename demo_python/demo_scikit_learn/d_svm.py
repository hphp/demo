#!/usr/bin/python

from sklearn import svm

def basic():
    X = [[0, 0], [1, 1] , [-1,-1]]
    y = [1, 1, 0]
    clf = svm.SVC()
    clf.fit(X, y) 
    print clf

def input_type():
    X = [[0, 0], [1, 1] , [-1,-1]]
    y = [1, 1, 0]
    print type(X),type(y),len(X),len(y) 

def if_could_get_trained_continuously():
    X = [[0, 0], [1, 1] , [-1,-1]]
    y = [1, 1, 0]
    clf = svm.SVC()
    clf.fit(X, y) 
    print clf.predict([2,2])
    X = [[3,3]]
    y = [0]
    clf.fit(X, y) 
    print clf.predict([2,2])
    X = [[4,4]]
    y = [0]
    clf.fit(X, y) 
    print clf.predict([2,2])
    X = [[2,2]]
    y = [0]
    clf.fit(X, y) 
    print clf.predict([2,2])

if_could_get_trained_continiously()    
#input_type()
