
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

def by_class_key():
    class Ele:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    rand_l = []
    for i in range(10):
        ele = Ele(i, random.randrange(120))
        rand_l += [ele]

    print rand_l
    #from operator import itemgetter, attrgetter
    rand_l = sorted(rand_l, key = lambda ele:ele.key) #itemgetter(0)) # ??????
    for ele in rand_l:
        print ele.key, ele.value
    rand_l = sorted(rand_l, key = lambda ele:ele.value) #itemgetter(0)) # ??????
    print '-----'
    for ele in rand_l:
        print ele.key, ele.value

def by_dic_key():
    rand_l = []
    for i in range(10):
        dic = {'x':i, 'y':10-i, 'z':random.randrange(120)}
        rand_l += [dic]
    rand_l = sorted(rand_l, key = lambda ele:ele['x'])
    for ele in rand_l:
        print ele
    print '-----'
    rand_l = sorted(rand_l, key = lambda ele:ele['y'])
    for ele in rand_l:
        print ele
    print '-----'
    rand_l = sorted(rand_l, key = lambda ele:ele['z'])
    for ele in rand_l:
        print ele
def sort_by_dict_order():
    arr = [ \
    "sdfdsfdsfs" \
    ,"abddfdsfds"\
    ,"sdfsdfs" \
    ,"dsfdsfs" \
    ,"dfdsfsfsfs" \
    ,"sdfds" \
    ]
    arr.sort()
    print arr
#basic()
#dim_2()
#by_class_key()
by_dic_key()
#sort_by_dict_order()
