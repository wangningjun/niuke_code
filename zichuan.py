def find_longest(str):
    result = 0
    length = len(str)
    for i in range(length):
        temp = str[i]
        for j in range(i+1, length):
            if str[j] not in temp:
                temp += str[j]
            else:
                break
        result = max(len(temp),result)
    return result

if __name__ == '__main__':
    str = input()
    res = find_longest(str)
    print(res)
