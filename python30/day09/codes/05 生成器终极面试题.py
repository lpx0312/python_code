def add(x,y):
    print("add func")
    return  x+y

def gen():
    print("gen func")
    yield 0
    yield 1
    yield 2
    yield 3

base = gen()  # 12345

for n in [1, 10]:
    base = (add(i, n) for i in base) # 23456
'''
base = (add(i, n) for i in 12345)
base = (add(i, n) for i in 23456)

n = 10
'''
print(list(base))
'''
 [add(i, 10) for i in (add(i, n) for i in 12345)]
 [add(i, 10) for i in (add(i, n) for i in gen())]
'''




def add(x,y):
    print("add func")
    return  x+y

def base():
    print("OK123")
    return [1,2,3]

base = (add(i, 10) for i in base())

# print(list(base))