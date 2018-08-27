from itertools import combinations
m = 5
a = [1,2,4,4,5]
c = 0
# b = list(combinations(a,2))
def conbin(a,count):
    if len(a) == 1:
        return count
    for i in range(1,len(a)):
        if a[0]^a[i] > m:
            count += 1
    count = conbin(a[1:],count)
    return count

count = conbin(a,c)
print(count)