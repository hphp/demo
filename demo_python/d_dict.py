
def basic():
    dic = {}
    dic[1] = 20
    dic['2'] = 30
#    print dic
    return dic

def iter():
    dic = {}
    dic[0] = 10
    dic[1] = 100
    dic[2] = 90
    for i in range(3):
        print dic[i]

def subdict():
    dic = {}
    dic[0] = {'x':1} #,{'z':3}}
    dic[1] = {'y':2} #,{'x',2}}
    print dic

    dic = {'x':1, 'y':2, 'z':3}
    print dic['x']

def array_dict():
    lst = []
    lst += [basic()]
    lst += [basic()]
    lst += [basic()]
    #lst[0:2]['2'] # not valid
    print lst

#iter()
#subdict()

array_dict()
