# -*- coding:utf-8 -*-
class Solution:

    def jumpFloor(self, n):

        if n< 0:
            return -1
        elif n-2 == 0:
            return 2
        elif n-1 ==0:
            return 1
        else:
            return self.jumpFloor(n-1)+self.jumpFloor(n-2)


if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(3))



