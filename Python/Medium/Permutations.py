# https://leetcode.com/problems/permutations/?envType=problem-list-v2&envId=backtracking

def permute(nums: list[int]):

    """ Youtube """
    # def backtrack(nums, path):
    #     if not nums:
    #         result.append(path)
    #         return
    #     for i in range(len(nums)):
    #         backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
    
    # result = []
    # backtrack(nums, [])
    # return result

    """ Neetcode """
    if len(nums) == 0:
        return [[]]

    perms = permute(nums[1:])
    res = []

    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p[:]
            p_copy.insert(i, nums[0])
            res.append(p_copy)
    
    return res

if __name__ == '__main__':

    n = list(map(int, input().split()))

    print(permute(n))