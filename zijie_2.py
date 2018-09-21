import sys
def CommonPrefix(strs):
    if not strs:
        return ''
    for i, item in enumerate(zip(*strs)):
        if len(set(item)) > 1:
            return strs[0][:i+1]
    return min(strs)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = []
    result = []
    for i in range(n):
        a.append(sys.stdin.readline().strip())
    for i in range(n):
        for j in range(n):
            if i != j:
                result.append(CommonPrefix([a[i],a[j]]))
    for i in range(n):
        print(max(result[i*(n-1):(n-1)*i+n-1]))
