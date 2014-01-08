
def basic():
    a = "abcd"
    b = "0123"
    c = "!@#$"

    sep = "."
    print sep.join((a,b,c)) #a.b.c
    print sep.join([a,b,c]) #a.b.c 
    print " ".join([a,b,c])

def strange():
    ns = "hellomorto-%08d!!"%(3+1)
    print ns

strange()
