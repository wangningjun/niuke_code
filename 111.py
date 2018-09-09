import time
N, K= 10,4
s = [1,0,1,0,1,0,0,0,1]

star = time.time()

for j in range(100000):
    sum = 0
    for i in range(len(s)):
        right = 1
        K_temp =K+1
        if s[i]==1:
            while i+right<len(s):
                if s[i+right] ==0:
                    K_temp -=1
                if K_temp ==0:
                    break
                right+=1
            sum = max(right,sum)
        else:
            continue
            # 等于0的完全是无需考的
            # K_temp -=1
            # while i+right<len(s):
            #     if s[i+right] ==0:
            #         K_temp -=1
            #     if K_temp ==0:
            #         break
            #     right+=1
            # sum = max(right,sum)

end = time.time()

print(sum, end-star)




