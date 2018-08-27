import sys

# n = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))
n = 92
A = [2, 76, 20, 6, 20, 10, 18, 34, 44, 2, 14, 30, 4, 84, 16, 4, 20, 10, 60, 10, 40,
     4, 4, 54, 10, 40, 40, 4, 30, 8, 10, 4, 4, 12, 28, 20, 20, 40, 4, 10, 12, 10, 6,
	 6, 12, 2, 18, 28, 4, 32, 2, 18, 8, 54, 56, 10, 18, 12, 20, 18, 50, 24, 30, 58,
	 42, 62, 28, 16, 6, 12, 22, 8, 34, 8, 14, 6, 78, 4, 8, 28, 6, 4, 20, 4, 52, 2,
	 28, 26, 38, 64, 10, 16]

len_a = len(A)
count = 0
sum_a = sum(A)
if sum_a % n != 0:
	print(-1)
else:
	av = sum_a / n
	for a in A:
		if (a - av) % 2 != 0:
			print(-1)
			exit()   # 结束程序
		else:
			count += abs(a - av)
	print(int(count / 4))
