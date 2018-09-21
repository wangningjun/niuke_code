import sys
content=list(map(int,sys.stdin.readline().split()))
num = 0
for temp in range(content[0],content[1]+1,1):
    tp=temp
    flag=True
    t1 = []
    while True:
        if tp>0:
            t1.append(tp%10)
            tp=int(tp/10)
            if tp>0:
                pass
            else:
                break

    lens = len(t1)-1

    if lens>0:
        for m in range(int(len(t1) / 2)):
            if t1[m] != t1[lens - m]:
                flag = True
            else:
                flag = False
                break
        if flag:
            num += 1
    else:
        num += 1

print(num)