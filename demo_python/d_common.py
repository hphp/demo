#!/usr/bin/python

def get_feature_index(l_id,l_N):
    index = 0 
    for i in range(len(l_N)):
        index *= l_N[i]
        index += l_id[i]
    return index

def test_get_feature_index():
    '''
    test with a 10*5 grid , with (i,j) = (2,3) , 
    index supposed to be 2*5 + 3 = 13

    test with a 10*5*2 grid , with (i,j,k) = (2,3,1) , 
    index supposed to be (2*5 + 3)*2 + 1 = 27

    test with a 10*5*2 grid , with (i,j,k) = (9,4,1) , 
    supposed to be 99

    '''
    l_id = [2,3]
    l_N = [10,5]
    print get_feature_index(l_id,l_N)
    l_id = [2,3,1]
    l_N = [10,5,2]
    print get_feature_index(l_id,l_N)
    l_id = [9,4,1]
    l_N = [10,5,2]
    print get_feature_index(l_id,l_N)

test_get_feature_index()
