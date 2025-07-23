from typing import List

def findLucky(arr: List[int]) -> int:
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    
    lukcy_int = -1

    for num in count.keys():
        if count[num] == num and num > lukcy_int:
            lukcy_int = num

    return lukcy_int

if __name__ == '__main__':

    case1 = [2, 2, 3, 4]
    case2 = [1, 2, 2, 3, 3, 3]
    case3 = [2, 2, 2, 3, 3]

    print(findLucky(case1))
    print(findLucky(case2))
    print(findLucky(case3))
    print(findLucky([3,4,3,4,3,4,2,4,2,1]))