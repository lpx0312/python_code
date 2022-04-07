#!/usr/bin/env python
# coding:utf-8
# 1.导入模块
import argparse

# 2.获取解析器对象
# 创建解析步骤
parser = argparse.ArgumentParser(description="Process some intergers.")

# 3.添加参数解析规则
# 添加参数步骤
parser.add_argument('integers',metavar='N',
                   type=int,nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum',dest='accumulator',
                   action='store_const',const=sum,default=max,
                   help='sum the integer')

# 4.解析参数
args = parser.parse_args()
print(args.accumulate(args.integers))
