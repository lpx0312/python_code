import  time

# 案例：计时案例

# 专门测 功能的运行时间
# 不用再每个函数中写这个功能
# def timer(f):
#     start = time.time()
#     f()
#     end = time.time()
#     print("花费时间",end-start)


# 如果现在要给 foo bar添加计时的功能，
# 可以添加timer这个高阶函数来实现，而且没有影响原有的foo和bar的代码，满足封闭功能
# 但是 外部如果想访问foo和bar的完整功能，包含foo和bar原有的打印功能，
# 就只能使用 timer(bar) timer(foo)，但是外部的接口 肯定是以原有的接口为准，外部肯定是调用圆口接口foo()和bar()
# 所以 不满足 开放的接口统一的 原则

# 现在就是需要 让 用户使用接口的时候，还是用老的 foo() 实现timer(foo)的功能
# 需求 foo()调用结果 等同于 timer(foo)
# 这时候就需要 使用闭包，


# 这就是 装饰器
# 主要用户 给函数新增功能，但是外部接口不变
# 这里timer称之为装饰器函数，inner是闭包函数，
def timer(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("花费时间", end - start)
    return inner

# 持续添加功能：
# 可以选择 那些功能需要新增功能，那些功能不需要添加功能，
def newfunc2(func):
    def inner(*args,**kwargs):
        func(*args, **kwargs)
        print("新增的第二个功能{}")
        # return  func(*args, **kwargs)
    return inner



# 这里bar（） 和 foo（）里面的内部 不更改  符合 封闭的原则
@newfunc2
def  bar(number):
    time.sleep(3) # 因为执行太快，所以加个2s 来显示
    print("bar功能{}".format(number))

# 使用@timer 相当于 foo = timer(foo) 说明foo函数包含了timer装饰器新增的功能
@timer
def foo():
    time.sleep(2) # 因为执行太快，所以加个2s 来显示
    print("foo功能")

# 但是由于这种写法太繁琐 而且还有顺序问题  所以不建议这样写，
# foo = timer(foo)    # 给foo添加timer的功能
# bar = timer(bar)    # 给bar也添加timer的功能
# foo()
# bar()


# # 但是由于这种写法太繁琐 而且还有顺序问题  所以不建议这样写，
# # foo = newfunc2(foo)         # 使用装饰器新增功能 新增foo的功能 不写bar就代表bar 没有新增功能
# # foo()

# 不带参数
# foo()

# 本身原功能带带参数
# bar(number="3")


# 原功能带参数，而且新的功能 再新加个参数【不推荐，因为更改了原有的函数bar的代码，(number,*args,**kwargs):】
# 但是如果原bar函数有参数，且又扩展参数*args,**kwargs，可使用这种用方法来使得装饰器带有参数。
def newfunc3(func):
    def inner(number,*args,**kwargs):
        func(number,*args, **kwargs)
        print("新增的第二个功能{}".format(kwargs["number2"]))
        # return  func(number,*args, **kwargs)
    return inner
@newfunc3
def  bar3(number,*args,**kwargs):
    time.sleep(3) # 因为执行太快，所以加个2s 来显示
    print("bar功能{}".format(number))
# bar3(number="3",number2="4")


# 装饰器，带有参数，需要这样
def newfunc4(text):
    def inner1(func):
        def inner2(number,*args,**kwargs):
            func(*args, **kwargs)
            print("新增的第二个功能{}".format(text))
            return  func(*args, **kwargs)
        return inner2
    return inner1

# 这个重点，装饰器带有参数
@newfunc4('newfunc4')
# 等价于 bar4()=newfunc4('newfunc4')(bar)
def  bar4(number,*args,**kwargs):
    time.sleep(3) # 因为执行太快，所以加个2s 来显示
    print("bar功能{}".format(number))
bar4(number="ss")


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def  bar4():
#     time.sleep(3) # 因为执行太快，所以加个2s 来显示
#     print("bar功能")
#
# bar4()







