def func_outer():
    x = 2
    print('x is', x)
    def func_inner():
        nonlocal x
        x = 5
    func_outer()
