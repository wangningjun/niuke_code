import sys
# 适合读取多列的数组
s = []
n = input()
for line in sys.stdin:
    if line =='\n':
        break
    a = line.split()
    s.append(a)

print(n,s)


