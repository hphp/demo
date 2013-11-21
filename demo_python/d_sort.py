
import random
def basic():
    l = range(100)
    rand_l = random.sample(l, 10)
    print rand_l
    rand_l.sort()
    print rand_l

def dim_2():
    l = range(100)
    dim_2_l = []
    for i in range(10):
        dim_2_l.append(random.sample(l,2))
    print len(dim_2_l),len(dim_2_l[0])
    print dim_2_l
    dim_2_l.sort()
    print dim_2_l

#basic()
dim_2()
