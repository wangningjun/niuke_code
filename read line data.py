'''
牛客网的数据读取方式
1.循环读取，直到输入空格后退出
'''
import sys
a = []
for line in sys.stdin:
    a.append(line.split())
    print(a)