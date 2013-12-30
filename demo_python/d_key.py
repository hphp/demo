import random
def basic(key_name):
    rand_l = []
    for i in range(10):
        dic = {'x':i, 'y':10-i, 'z':random.randrange(120)}
        rand_l += [dic]
    rand_l = sorted(rand_l, key = lambda ele:ele[key_name])
    for ele in rand_l:
        print ele[key_name]

basic('x')
print '----'
basic('y')
print '----'
basic('z')
