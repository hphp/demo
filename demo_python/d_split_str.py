
def basic():
    s = "cat.5.jpg"
    slist = s.split(".")
    for i in slist:
        print i

def multi_char():
    s = "cat..5.jpg..kk."
    for i in s.split("."):
        print '-'+i+'-'

multi_char()
