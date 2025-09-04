# https://leetcode.com/problems/reverse-bits/description/


def reverseBits(n: int) -> int:
    res = 0

    for i in range(32):
        bit = (n >> i) & 1
        res |= (bit << (31 - i))
    
    return res



if __name__ == '__main__':

    case = 43261596
    print(reverseBits(case))
    case = 2147483644
    print(reverseBits(case))