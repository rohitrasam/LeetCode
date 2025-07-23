# https://leetcode.com/problems/kth-distinct-string-in-an-array/?envType=problem-list-v2&envId=hash-table


from collections import Counter
from typing import List


def kthDistinct(arr: List[str], k: int) -> str:
    count = Counter(arr)
    dist = []

    for s in count:
        if count[s] == 1:
            dist.append(s)

    
    return "" if k-1 > len(dist) else dist[k-1]



if __name__ == '__main__':
    
    case = ["d","b","c","b","c","a"], 2
    print(kthDistinct(*case))
    case = ["aaa","aa","a"], 1
    print(kthDistinct(*case))
    case = ["a","b","a"], 3
    print(kthDistinct(*case))
