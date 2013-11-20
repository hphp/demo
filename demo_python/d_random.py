
import random

def over_range():
    a = random.randrange(0,-1)
    print a

def generate_random_list():
    feature = []
    for i in range(2500):
        feature.append(random.randrange(0,256))
    l = random.sample(feature,10)
    print l

def random_list():
    ll = []
    for i in range(200):
        ll.append(i)

    nl = random.sample(ll,10)
    print nl

#random_list()
#generate_random_list()
over_range()
