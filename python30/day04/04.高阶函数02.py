#
def foo():
    def bar():
        print("bar")
        #没有返回值 默认是None
    return bar

foo()  # None

#
def foo(x):
    def bar(x):
        print(x)
    return bar(x)

foo("hah")


