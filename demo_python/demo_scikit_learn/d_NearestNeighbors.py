#!/usr/bin/python
from sklearn.neighbors.nearest_centroid import NearestCentroid

import numpy

X = numpy.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
y = numpy.array([1,1,1,2,2,2])

clf = NearestCentroid()
clf.fit(X,y)

NearestCentroid(metric='euclidean', shrink_threshold=None)
print clf.predict([0,1])
