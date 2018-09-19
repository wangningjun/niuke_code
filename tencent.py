import sys
def lcm(x, y,z):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y ==z )):
            lcm = 1
            break
        greater += 1
        if greater >= x*y+z:
            lcm = 0
            break
    return lcm




if __name__ == '__main__':

    n = int(sys.stdin.readline().strip())
    maps = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        maps.append(values)

    for i in range(n):
        a =lcm(maps[i][0], maps[i][1],maps[i][2])
        if a ==1:
            print('Yes')
        else:
            print('No')
    # a = list(map(int,sys.stdin.readline().strip().split()))
    # print(a)

