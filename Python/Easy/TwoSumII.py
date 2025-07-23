from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    low = 0
    high = len(numbers) - 1

    while low < high:
        if numbers[low] + numbers[high] > target:
            high -= 1
        elif numbers[low] + numbers[high] < target:
            low += 1
        else:
            return low+1, high+1


if __name__ == '__main__':

    case4 = [3,24,50,79,88,150,345], 200
    print(twoSum(*case4))
