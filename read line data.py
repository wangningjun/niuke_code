'''
牛客网的数据读取方式
1.循环读取，直到输入空格后退出,使用line
'''
# import sys
# a = []
# for line in sys.stdin:
#     a.append(line.split())
#     print(a)
#
'''
2.循环读取，使用input()
'''

n = int(input())
A = map(int, input().split())
k, d = map(int, input().split())
