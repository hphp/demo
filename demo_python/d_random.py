
import random

def over_range():
    a = random.randrange(0,-1)
    print a

def generate_random_list(n):
    feature = []
    for i in range(n):
        feature.append(random.randrange(0,256))
    l = random.sample(feature,10)
    print l

def random_list():
    ll = []
    for i in range(200):
        ll.append(i)

    nl = random.sample(ll,10)
    print nl

def random_basic():
    print random.randrange(1000)
#random_list()
#generate_random_list()
#over_range()
#random_basic()
generate_random_list(200)
