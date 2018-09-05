n = int(input())

# a = list(map(int, raw_input().split()))  #低版本的
a = list(map(int, input().split()))
left = 0
right = len(a)-1
if len(a)==1:
    print("yes")
for i in range(len(a)):
    if a[left]<a[left+1]:
        left += 1
    if a[right-1]<a[right]:
        right -= 1

    if a[left]>a[left+1] and a[right-1]>a[right]:
        break

b = a[left:right+1]
if b[::-1] == sorted(b)and b[0]<a[right+1]:
    print("yes")
else:
    print("no")

# x = input()
#
# x = [int(i) for i in x.split()]
# y = [ i for i in x]
# print(y)
