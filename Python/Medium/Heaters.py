import bisect
from typing import List

def findRadius(houses: List[int], heaters: List[int]) -> int:
    houses.sort()
    heaters.sort()

    result = 0

    for house in houses:
        left = bisect.bisect_right(heaters, house) - 1
        right = bisect.bisect_left(heaters, house)

        if left < 0:
            result = max(result, heaters[0] - house)
        elif right >= len(heaters):
            result = max(result, house - heaters[-1])
        else:
            result = max(result, min(house - heaters[left], heaters[right] - house))

    return result


if __name__ == '__main__':

    case1 = [1, 2, 3], [2]
    case2 = [1, 2, 3, 4], [1, 4]
    case3 = [1, 5], [2]

    print(findRadius(*case1))
    print(findRadius(*case2))
    print(findRadius(*case3))
