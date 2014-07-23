
def basic():
    backslash = "\\"
    print backslash
    backslash = r'\adfsfd\dfdsfsd'
    print backslash

def join():
    backslash = r''
    lst = ['dsfds',r'\"sdfds\"','"dfsfds"dsfds']
    backslash = ".".join(lst)
    print backslash

def print_raw():
    formatstr = "%r %r %r %r"
    lst = ['dsfds',r'\"sdfds\"','"dfsfds"dsfds', '\"hello morto\"']
    print formatstr % (lst[0], lst[1], lst[2], lst[3])

print_raw()
