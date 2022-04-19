#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：python_code 
@File    ：xml_demo01.py
@Author  ：lipanxiang
@Date    ：2022/4/19 23:32 
'''


#!/usr/bin/python
#coding:utf-8
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except Exception as e:
    pass
'''
参考文档： https://blog.csdn.net/weixin_39274753/article/details/82221859
'''
try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET

with open('xml_demo01.xml', 'r') as f:
    xml_string = f.read()

#从变量读取，参数为XML段，返回的是一个根Element对象
root = ET.fromstring(xml_string)  # 等价于 ET.parse('1.xml') + tree.getroot()

#从xml文件中读取，用getroot获取根节点，根节点也是Element对象
# tree = ET.parse('1.xml')
# root = tree.getroot() # root是一个Element，但是根本没有属性 print root.tag, root.attrib 什么都没有

# tag = root.tag
# attrib = root.attrib
# value = root.text
# print tag,attrib,value

# 遍历子元素
for child in root:
    print(child.tag, child.attrib)
# 通过索引值来访问特定的子元素
print(root[0])  # Element对象
print(root[0].tag)  # 标签名
print(type(root[0].tag))  # 标签名 字符串
print(root[0].attrib)  #属性
print(type(root[0].attrib)) # 字典
print(root[0].get('name')) # Liechtenstein 只能通过get获取，不能通过索引获取。
if root[0].text == '\n        ':
    print( "value存在")
    print(repr(root[0].text))  # '\n        '
    print( type(root[0].text))  # 字符串，但好像打印出来是空，这里不准，

print( '================================')

print ('遍历某一Element对象下 所有子元素')
for elem in root[0].iter():
    print( elem.tag,elem.attrib)

print( '================================')
print ('遍历某一Element对象下 tag=\'neighbor\' 为 所有子元素,但是iter不要加tag=neighbor,直接用位置参数 neighbor，加tag=容易出现问题')
for elem in root[0].iter('neighbor'):
    # print elem
    print (elem.tag,elem.attrib)


print ('================================')
print ('find方法会返回第一个匹配的子元素，只能查找直接子元素')
firstCountry = root.find("country")
print(firstCountry.attrib['name'])

print( '================================')
print ('findall以列表的形式返回所有匹配的子元素,注意findall只能查找直接子元素，不能用来查找rank，neighbor等element')
for elem in root[0].findall('neighbor'):
    print( elem.tag, elem.attrib, elem.text)

print( '================================')
print( 'iterfind则返回一个所有匹配元素的迭代器（iterator），iterfind 也只能查找直接子元素。')
for elem in root[0].iterfind('neighbor'):
    print( elem.tag,elem.attrib,elem.text)

print( "++++++++++++++++++++++++++++++++++++++++++++++++++")
print( "扩展，因为find findall iterfind 都只能查询直接子元素，不能隔级查询，所有需要使用XPATH来扩展查询")

print( '================================')
print( 'find的xpath用法')
firstCountry = root.find("country/neighbor")
print(firstCountry.attrib['name'])

print( 'findall的xpath用法,查找tag=country元素下tag=neighbor的所有元素')
for elem in root.iterfind('country/neighbor'):
    print( elem.tag,elem.attrib,elem.text)

print( "iterfind的xpath形式，查找tag=country元素下tag=neighbor的所有元素")
for elem in root.iterfind('country/neighbor'):
    print( elem.tag,elem.attrib,elem.text)


'''
文档中，还有XML的构建，和利用iterparse解析XML流 后续再研究
XPATH教程：https://www.w3school.com.cn/xpath/xpath_syntax.asp

# 参考2：https://blog.csdn.net/sinat_34461199/article/details/116106144
'''
