import math
class Solution:
    def Fibonacci(self, n):
        # write code here
        a = math.sqrt(5)/5
        b = (1+math.sqrt(5))/2
        c = (1-math.sqrt(5))/2
        result = a*(math.pow(b,n)-math.pow(c,n))

        return result


if __name__ == '__main__':
    for i in range(1,10):
        print(int(Solution().Fibonacci(i)))