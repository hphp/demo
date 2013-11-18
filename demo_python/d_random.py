
import random

def random_list():
    ll = []
    for i in range(200):
        ll.append(i)

    nl = random.sample(ll,10)
    print nl

random_list()
