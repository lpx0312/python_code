# # 内层函数，引用外部自由变量的时候，则内存函数式闭包函数
# # 函数调用结束后，函数里面的变量就都没有了
# def outer():
#     x = 10
#     def inner():  # 引用了外部变量，则inner是闭包函数
#         print(x)
#     return inner
#
#
#
# func = outer()
# # 这里outer函数调用结束，则应该x =10 会包销毁。
# # 但是 因为 inner()调用了，外部的变量x，符合闭包函数，则解释器，会保存这个x=10变量，
# # 下次闭包inner调用x的时候，可以取到
# # 也就有个缺点，这个x=10变量会一直存在，
# func()

# # 这里和上边一样，inner依旧是闭包函数
def outer(x):
    # 和x = 10 是一样的
    def inner():  # 引用了外部变量，则inner是闭包函数
        print(x)
    return inner
func = outer(20)
func()






