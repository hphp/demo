
import cPickle
import theano
import theano.tensor as T
import numpy

class d_pickle_TEMPLATE():
    def __init__(self,v=0,m=2,n=150):
        self.v = v 
        self.m = m
        self.n = n

    def __getstate__(self):
        return (self.m, self.n)

    def __setstate__(self, state):
        m, n = state
        self.m = m
        self.n = n

class d_pickle_Tensor_TEMPLATE():
    def __init__(self,input,W_shape,W = None):
        self.input = input
        if W == None :
            self.W = theano.shared(value=numpy.zeros(W_shape, \
                dtype=theano.config.floatX), \
                name='W', borrow=True)
        else:
            self.W = W
        self.b = 1

        self.output = T.dot(self.input,self.W) + 3

    def __getstate__(self):
        return (self.W,self.b)

    def __setstate__(self, state):
        W,b = state
        self.W = W
        self.b = b

def dump_tensor_obj():
    x = T.ivector('x')
    tensor_obj = d_pickle_Tensor_TEMPLATE(input=x,W_shape=(2,2))
    updates = [(tensor_obj.W,tensor_obj.W + tensor_obj.output)]

    #y = T.dot(x, W) +234
    f = theano.function(inputs = [x],
    outputs= tensor_obj.output,
    updates = updates)
    print f([2,2])
    print f([2,2])
    to_state = tensor_obj.__getstate__()
    print type(to_state),type(to_state[0]),to_state[0].get_value()
    file_t = open('tmp.file','w')
    cPickle.dump(to_state,file_t)
    file_t = open('tmp.file','r')
    state = cPickle.load(file_t)

    W , b = state
    print W
    d = d_pickle_Tensor_TEMPLATE(input=x,W_shape=(2,2),W=W)

    f_d = theano.function(inputs = [x],
    outputs= d.output)

    print f_d([1,1])
    print f_d([1,1])
    print f_d([1,1])

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

def dump_obj():
    c = d_pickle_TEMPLATE(-2,10,5)
    c_state = c.__getstate__()
    file_t = open('tmp.file','w')
    cPickle.dump(c_state,file_t)
    file_t = open('tmp.file','r')
    state = cPickle.load(file_t)
    d = d_pickle_TEMPLATE()
    print d.__getstate__()
    d.__setstate__(c_state)
    print d.__getstate__()
    d.__setstate__(state)
    print d.__getstate__()

#diff_type_obj()
#dump_obj()
dump_tensor_obj()
