
class Payment(object):
    def __init__(self,name,money):
        self.money=money
        self.name=name

    def pay(self,*args,**kwargs):
        pass

class AliPay(Payment):
    def pay(self):
        # 支付宝提供了一个网络上的联系渠道
        print('%s通过支付宝消费了%s元'%(self.name,self.money))

class WeChatPay(Payment):

    def pay(self):
        # 微信提供了一个网络上的联系渠道
        print('%s通过微信消费了%s元'%(self.name,self.money))

class Cash:
    def __init__(self, name, money):
        self.money = money
        self.name = name

    def pay(self):
         # 支付宝提供了一个网络上的联系渠道
         print('%s通过现金消费了%s元' % (self.name, self.money))


# 测试类
class Order(object):
    def account(self,pay_obj):
        pay_obj.pay()

wc = WeChatPay("yuan",100)
ali = AliPay("alex",200)
cash = Cash("alvin",230)

order = Order()
order.account(cash)