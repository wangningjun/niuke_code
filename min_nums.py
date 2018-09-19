class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray==[]:
            return 0
        left = 0
        right = len(rotateArray) - 1

        while right>left:
            if rotateArray[left]<rotateArray[right]:
                 return rotateArray[left]

            middel = left + (right -left)//2

            if rotateArray[left]<rotateArray[middel]:
                left =middel+1
            elif rotateArray[right]>rotateArray[middel]:
                right = middel
            else:
                left+=1
        return rotateArray[right]

if __name__ == '__main__':
    a = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
    b = Solution().minNumberInRotateArray(a)
    print(b)



