from collections import defaultdict

'''
实现输入字符串的
'''
dd = defaultdict(int)

for i in input():
	if i.isalpha():
		dd[i] +=1
		if dd[i] ==3:
			print(i)
			break