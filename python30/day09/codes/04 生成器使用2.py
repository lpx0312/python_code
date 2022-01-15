


# def foo():
#     count = 0
#     while count<4:
#         yield count
#         count+=1
#
# gen = foo() # 创建生成器对象
# print(gen.__next__()) # next(gen)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# 生成器创建方式两种：1 函数+yield构建  2 （）

# 列表生成式
# l = []
# for x in range(4):
#     l.append(x*x)
# print(l) # [0, 1, 4, 9]
#
# print([i*i+1 for i in range(4)])

# 生成器创建方式2：
gen = (i*i+1 for i in range(1000000000))
print(gen) # <generator object <genexpr> at 0x0000024602D959E8>
# print(next(gen))
# print(next(gen))
# print(next(gen))
for i in gen:
    print(i)
