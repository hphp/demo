
def basic():
    dic = {}
    dic[1] = 20
    dic['2'] = 30
    print dic

def iter():
    dic = {}
    dic[0] = 10
    dic[1] = 100
    dic[2] = 90
    for i in range(3):
        print dic[i]

iter()
