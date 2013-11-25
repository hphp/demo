
import numpy as np
import scipy
import scipy.sparse
import spams

if not ('rand' in scipy.sparse.__dict__):
    import myscipy as ssp 
else:
    import scipy.sparse as ssp 
    m=200; n = 200000; d= 0.05
    A = ssp.rand(m,n,density=d,format='csc',dtype=np.float64)
#    B = spams.CalcAAt(A)

