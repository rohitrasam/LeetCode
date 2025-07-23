from typing import List

def gcd(a: int, b: int):
    smaller = min(a, b)
    greater = max(a, b)

    while greater % smaller != 0:
        rem = greater % smaller
        greater = smaller
        smaller = rem

    return smaller 

def replaceNonCoprimes(nums: List[int]) -> List[int]:

    i = 0
    stack = []
    gcd_val = 0
    while i <= len(nums):
        while len(stack) >= 2 and (gcd_val := gcd(stack[-1], stack[-2])) > 1:
            x, y = stack.pop(), stack.pop()
            lcm = int((x * y) / gcd_val)
            stack.append(lcm)
        if i < len(nums):
            stack.append(nums[i])

        i += 1

    return stack 

if __name__ == '__main__':
    case1 = [6,4,3,2,7,6,2]
    case2 = [2,2,1,1,3,3,3]
    case3 = [287,41,49,287,899,23,23,20677,5,825]
    case4 = [10, 3, 2, 14, 6, 7, 9]

    # print(gcd(4, 3))
    # print(gcd(6, 4))
    # print(gcd(24, 6))
    print(replaceNonCoprimes(case1))
    print(replaceNonCoprimes(case2))
    print(replaceNonCoprimes(case3))
    print(replaceNonCoprimes(case4))
