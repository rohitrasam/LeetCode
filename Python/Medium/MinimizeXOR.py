# https://leetcode.com/problems/minimize-xor/editorial/?envType=daily-question&envId=2025-01-15

def minimizeXor(num1: int, num2: int) -> int:
    
    res = num1
    cnt1 = bin(num1).count('1')
    cnt2 = bin(num2).count('1')
    i = 0

    while cnt1 > cnt2:
        if res & (1 << i):
            cnt1 -= 1
            res = res ^ (1 << i)

        i += 1

    while cnt1 < cnt2:
        if res & (1 << i) == 0:
            cnt1 += 1
            res |= (1 << i)
        i += 1
    
    return res



if __name__ == '__main__':
    case1 = 3, 5
    case2 = 1, 12

    print(minimizeXor(*case1))
    print(minimizeXor(*case2))