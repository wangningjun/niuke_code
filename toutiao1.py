# n = int(input())
# A = list(map(int,input().split()))
n = 4
A = [20,35,23,40]


A.sort()
A.append(200)
print(A,len(A))

count =0
j = 0
for i in range(1,len(A)):
    if(A[i]-A[i-1])<=10 :
        j+=1
    else:
        if j % 3 == 0:
            count = count+2
            j = 0
        if j % 3 == 1:
            count = count + 1
            j =0
        if j%3==2:
            j = 0


print(count)