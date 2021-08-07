def foo(*args):
    for arg in args:
        print(arg+" ", end="")
    print()

foo('a', 'b')
foo('a', 'b', 'c')

