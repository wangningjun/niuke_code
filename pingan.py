import sys

def versionCompare(v1, v2):

    v1_list = v1.split(".")
    v2_list = v2.split(".")
    v1_len = len(v1_list)
    v2_len = len(v2_list)
    if v1_len > v2_len:
        for i in range(v1_len - v2_len):
            v2_list.append(None)
    elif v2_len > v1_len:
        for i in range(v2_len - v1_len):
            v1_list.append(None)
    else:
        pass
    for i in range(len(v1_list)):
        if v1_list[i]==None:
            return False
        if v2_list[i]==None:
            return True
        if int(v1_list[i]) > int(v2_list[i]):
            return True
        if int(v1_list[i]) < int(v2_list[i]):
            return False
    return True

def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and versionCompare(L[j],key):
            j = j - 1
        L[i] = L[j]
        while i < j and versionCompare(key,L[j]):
            i = i + 1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i - 1)
    quickSort(L, j + 1, high)
    return L

def bubble(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        for i in range(listLength - 1):
            if versionCompare(bubbleList[i],bubbleList[i+1]):
                temp= bubbleList[i+1]
                bubbleList[i+1] = bubbleList[i]
                bubbleList[i] = temp
        listLength -= 1
    return (bubbleList)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a=[]
    # v1 = '1.2.0.0'
    # v2 = '1.2'
    for i in range(n):
        a.append(sys.stdin.readline().strip())
    s1 = bubble(a)
    # s = quickSort(a,0,len(a)-1)
    for i in s1:
        print(i)




