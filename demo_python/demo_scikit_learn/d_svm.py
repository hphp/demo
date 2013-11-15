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

input_type()
