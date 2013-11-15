#!/usr/bin/python

from sklearn import svm
X = [[0, 0], [1, 1] , [-1,-1]]
y = [1, 1, 0]
clf = svm.SVC()
clf.fit(X, y) 
print clf
