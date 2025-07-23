from typing import List


def countCompleteDayPairs(hours: List[int]) -> int:
    hashmap = {}
    count = 0
    for idx in range(len(hours)):
        x = 24 - hours[idx] % 24
        if x in hashmap:
            count += hashmap[x]
            hashmap[x] += 1
        else:
            hashmap[x] = 1

    return count


if __name__ == '__main__':
    
    case1 = [12,12,30,24,24]
    case2 = [72,48,24,3]
    case3 = [12, 36, 30]

    print(countCompleteDayPairs(case1))
    print(countCompleteDayPairs(case2))
    print(countCompleteDayPairs(case3))
