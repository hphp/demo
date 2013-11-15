#!/usr/bin/python

from sklearn import svm
import cPickle

def dump_in_pickle():
    X = [[0, 0], [1, 1] , [-1,-1]]
    y = [2, 2, 0]
    clf = svm.SVC()
    clf.fit(X, y) 
    #clf_ori = svm.SVC()
    #print clf_ori.predict([0,1])
    # it is inappropiat
    clf_file = open("clf.tmp","w")
    clf_pickle = cPickle.dump(clf,clf_file)
    print clf

def write_from_pickle():
    clf_file = open("clf.tmp","r")
    clf = cPickle.load(clf_file)
    print type(clf)
    print clf.predict([0,1])

#dump_in_pickle()
write_from_pickle()
