n = int(input())
A = map(int,input().split())

B = [i for i in A]

B.sort()
B.append(200)
count =0
j = 0
for i in range(1,len(B)):
    if(B[i]-B[i-1])<=10 :
        j+=1
    else:
        if j%3==2:
            count = count+2
        if j%3==1:
            j = 0
        if j%3==0:
            count = count+1

print(count)