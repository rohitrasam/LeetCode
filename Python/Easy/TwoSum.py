def twoSum(nums: list[int], target: int) -> list[int]:

    hashmap = {}

    for idx in range(len(nums)):
        x = target - nums[idx]
        if x in hashmap:
            return idx, hashmap[x]
        hashmap[nums[idx]] = idx

if __name__ == '__main__':
    target = 9
    arr = [2,7,11,15]


    print(twoSum(arr, target))