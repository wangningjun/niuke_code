#
# s = input()
# n = int(s)
# valu = 1
# count = 1
# temp = 1
# for i in range(1, n):
#
#     if count == 0:
#         valu -= 1
#         temp += 1
#         count = temp
#     else:
#         valu += 1
#         count -= 1
#
# print(valu)

def get_value(day):
    day = int(day)
    days = 1
    mv = -2
    inc = 2
    while day >= days:
        days += inc
        inc += 1
        mv += 2
    return (day - mv)
while 1:

    day = input()
    print(get_value(day))
