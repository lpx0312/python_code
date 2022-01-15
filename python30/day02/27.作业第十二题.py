'''
4、输出商品列表，用户输入序号，显示用户选中的商品
    商品 li = ["手机", "电脑", '鼠标垫', '游艇']
要求：1：页面显示 序号 + 商品名称，如：
      	1 手机
	   	2 电脑
     2： 用户输入选择的商品序号，然后打印商品名称
     3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
     4：用户输入Q或者q，退出程序。
'''

li = ["手机", "电脑", '鼠标垫', '游艇']
for index,value in enumerate(li):
    print(index+1,value)


while 1:
    count = input("请输入商品序号>>>>：")
    if count == "q" or count == "Q":
        print("程序退出")
        exit()

    if count.isdigit():
        count = int(count)
        if 1 <= count <= len(li) :
            print("商品名称是{}".format(li[count - 1]))
        else:
            print("输入的商品序号，不存在")
    else:
        print("请输入需要的数字，不要输入其他的")

