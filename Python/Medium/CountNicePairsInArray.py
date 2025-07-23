# https://leetcode.com/problems/count-nice-pairs-in-an-array/description/?envType=problem-list-v2&envId=hash-table


from typing import List


def countNicePairs(nums: List[int]) -> int:
    def rev(x: int) -> int:
        # return int(str(x)[::-1].lstrip('0'))

        rev_num = 0
        while x != 0:
            rem = x % 10
            rev_num = rem + rev_num * 10
            x //= 10
        
        return rev_num
    
    seen = {}
    count = 0
    for num in nums:
        diff = num - rev(num)
        if diff in seen:
            count += seen[diff]
            seen[diff] += 1
        else:
            seen[diff] = 1
    
    return count % (10**9 + 7)



if __name__ == '__main__':

    case = [42,11,1,97]
    print(countNicePairs(case))
    case = [13,10,35,24,76]
    print(countNicePairs(case))
