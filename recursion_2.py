class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number ==0:
            return 0
        lis = [1 for _ in range(number+1)]

        for i in range(2,number+1):
            lis[i] = 0
            for j in range(i):
                lis[i] = lis[i]+lis[j]
        return lis[number]

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloorII(4))