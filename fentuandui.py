import sys


def get_total(i, j, n, m, map):
    seat = [[i, j]]
    sum_map = map[i][j]
    while seat:
        i, j = seat[0][0], seat[0][1]
        for a in zip((0, 1, 0, -1), (-1, 0, 1, 0,)):

            if -1 < (a[0] + i) < n and -1 < (a[1] + j) < m and map[i + a[0]][j + a[1]] != 0:
                seat.append([i + a[0], j + a[1]])
                sum_map += map[i + a[0]][j + a[1]]
                map[i + a[0]][j + a[1]] = 0
        del seat[0]
    return sum_map

if __name__ == '__main__':

    n = int(sys.stdin.readline().strip())
    maps = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        maps.append(values)
    num = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] != 0:
                num.append(get_total(i, j, n, n, maps))
    len_num = len(num)
    print(len_num)



# import sys
#
# def get_total(i, j, n, m,map):
#     seat = [[i,j]]
#     sum_map = map[i][j]
#     while seat:
#         i , j = seat[0][0],seat[0][1]
#         for a in zip((0, 1, 0, -1), (-1, 0,  1, 0,)):
#
#             if -1<(a[0]+i)<n and -1<(a[1]+j)<m and map[i+a[0]][j+a[1]] !=0:
#                 seat.append([i+a[0],j+a[1]])
#                 sum_map +=map[i+a[0]][j+a[1]]
#                 map[i + a[0]][j + a[1]] = 0
#         del seat[0]
#
#     return sum_map
#
#
# if __name__ == '__main__':
#
#     n = int(sys.stdin.readline().strip())
#
#     maps = []
#     for line in sys.stdin:
#         if line == '\n':
#             break
#         # a = line.split()
#         values = list(map(int, line.split()))
#         maps.append(values)
#     # n = 4
#     # maps = [[1 ,0 ,0 ,0],[0 ,0 ,0 ,0],[0 ,0 ,0 ,1],[0 ,0 ,0 ,0] ]
#
#
#     num = []
#     for i in range(n):
#         for j in range(n):
#             if maps[i][j] !=0:
#                 num.append(get_total(i,j,n,n,maps))
#     len_num = len(num)
#
#     print(len_num)
