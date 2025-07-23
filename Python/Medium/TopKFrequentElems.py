from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freqs = [[] for _ in range(len(nums))]

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for item, value in count.items():
        freqs[value].append(item)
    
    res = []
    for freq in freqs[::-1]:
        for f in freq:
            res.append(f)
            if len(res) == k:
                return res
 
if __name__ == '__main__':
    case1 = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
    print(topKFrequent(case1, 2))