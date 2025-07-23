def majority(nums: list[int]) -> int:
    
    """ Boyre Moore Voting Algo """
    count = 0
    candidate = nums[0]

    for num in nums:
        if num == candidate:
            count += 1
        elif count == 0:
            candidate = num
        else:
             count -= 1
    
    return candidate


    """Leetcode user solution"""
    # return max(set(nums), key=nums.count)

    """ My Solution"""
    # counts ={}

    # for num in nums:
    #     if num in counts:
    #         counts[num] += 1
    #     else:
    #         counts[num] = 1

    # return sorted(counts.items(), key=lambda x: x[1], reverse=True)[0][0] 



if __name__ == '__main__':
    n = list(map(int, input().split()))

    print(majority(n))
