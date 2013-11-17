
import cPickle

class d_pickle_TEMPLATE():
    def __init__(self,b):
        self.v = b

def basic():
    list_l = [0,2,3,1,4,9]
    file_t = open('tmp.file','w')
    cPickle.dump(list_l,file_t)
    file_t = open('tmp.file','r')
    test_l = cPickle.load(file_t)
    print type(test_l),test_l

def diff_type_obj():
    a = [9,2,4]
    b = 3.8
    c = d_pickle_TEMPLATE(-2)
    list_l = [a,b,c]
    file_t = open('tmp.file','w')
    cPickle.dump(list_l,file_t)
    file_t = open('tmp.file','r')
    test_l = cPickle.load(file_t)
    if isinstance(test_l,list):
        print "test_l is a list"
        for ele in test_l:
            print type(ele),ele
            if isinstance(ele,d_pickle_TEMPLATE):
                print "ele is a d_pickle_TEMPLATE obj , with v: ", ele.v
    else:
        print type(test_l)

diff_type_obj()
