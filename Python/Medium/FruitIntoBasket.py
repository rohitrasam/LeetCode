# https://leetcode.com/problems/fruit-into-baskets/description/?envType=problem-list-v2&envId=hash-table


from typing import List


def totalFruit(fruits: List[int]) -> int:
    l = 0
    max_len = 0
    types = {}
    types[fruits[0]] = 1

    for r in range(1, len(fruits)):
        if fruits[r] not in types:
            max_len = max(max_len, r - l)
            types[fruits[r]] = 1
            while len(types) != 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    types.pop(fruits[l])
                l += 1
        else:
            types[fruits[r]] += 1
    return max(max_len, sum(types.values()))


if __name__ == '__main__':


    case = [1,2,1]
    print(totalFruit(case))
    case = [0,1,2,2]
    print(totalFruit(case))
    case = [1,2,3,2,2]
    print(totalFruit(case))
    case = [0,1,2,1,2,2,3,2,3,3,2,2]
    print(totalFruit(case))