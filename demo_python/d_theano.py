from theano import *
import theano.tensor as T

def basic():
    W = T.dmatrix('W')
    v = T.dvector('v')
    x = T.dvector('x')
    y = T.dot(x, W) +234
    VJ = T.Lop(y, W, v)
    theano.printing.debugprint(VJ) 
    '''
    dot [@A] ''   
     |DimShuffle{0,x} [@B] ''   
      | |DimShuffle{0} [@C] 'x.T'   
       |   |x [@D]
        |DimShuffle{x,0} [@E] ''   
           |v [@F]
    '''
    f = function([W, x], y) # runs ok
    print f([[1, 1], [1, 1]],  [0, 1])
    #f([[1, 1], [1, 1]], [2, 2], [0, 1])

    #f = function([W, v, x], VJ) # error :theano.compile.function_module.UnusedInputError: , because of W.
    f = function([v, x], VJ) # error :theano.compile.function_module.UnusedInputError: , because of W.
    print f([0,1],[1,1])

