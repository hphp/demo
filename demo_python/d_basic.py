
def pass_arg():
    a = 1
    b = {}
    b['hello'] = 'world'
    b['hi'] = 'nimei'
    def test_pass_arg(a, b):
        a = 2
        b['hello'] = 'hello world'
        b['aa'] = 'bbb'

    test_pass_arg(a, b)
    # here demonstrate that pass a obj , it is passed as the 'reference' , but for the regular variable, it will set a temporary variable to replace the original one.
    print a
    print b

pass_arg()
