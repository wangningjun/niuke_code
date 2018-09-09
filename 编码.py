import sys

def validUtf8(data):
    """
    :type data: List[int]
    :rtype: bool
    """
    masks = [0x0, 0x80, 0xE0, 0xF0, 0xF8]
    bits = [0x0, 0x0, 0xC0, 0xE0, 0xF0]
    while data:
        for x in (4, 3, 2, 1, 0):
            if data[0] & masks[x] == bits[x]:
                break
        if x == 0 or len(data) < x:
            return 0
        for y in range(1, x):
            if data[y] & 0xC0 != 0x80:
                return 0
        data = data[x:]
    return 1
if __name__ == '__main__':

    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    str_ = list(map(int, line.split()))
    print(validUtf8(str_))