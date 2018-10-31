import sys
'''
采用归并排序的方式在排序的同时统计逆序数的个数
2018/09/26
'''

def InNum(lst):
    if len(lst) == 1:
        return lst, 0
    else:
        n = len(lst) // 2
        lst_1, count1 = InNum(lst[0:n])
        lst_2, count2 = InNum(lst[n:len(lst)])
        lst, count = Count(lst_1, lst_2, 0)
        return lst, count1 + count2 + count  # 逆序数个数 = 左半部分+右半部分+左右之间的个数

def Count(lst_1, lst_2, count):
    i = 0
    j = 0
    res = []
    while i < len(lst_1) and j < len(lst_2):  #一旦一个出现溢出就停止，往后的都会符合条件
        if lst_1[i] <= lst_2[j]:
            res.append(lst_1[i])
            i += 1
        else:
            res.append(lst_2[j])
            count += len(lst_1) - i   # 往后的所有数都可以形成逆序数
            j += 1
    res += lst_1[i:]
    res += lst_2[j:]
    return res, count



if __name__ == '__main__':
    # # n = int(input())
    # line = sys.stdin.readline().strip()
    # nums_o = list(map(int, line.split()))
    # b = 100000
    # j = 0
    # for i in range(len(nums_o)):
    #     nums = nums_o.copy()
    #     nums[i] = 0
    #     _,a = InNum(nums)
    #     if b > a:
    #         b = a
    #         j = i
    #
    # print(b,j+1)
    print(InNum([2,5,4,3,1]))



