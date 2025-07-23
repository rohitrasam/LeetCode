def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:

    res = {}
    mini = len(list1) + len(list2) - 2
    i = 0
    j = 0

    while i < len(list1):
        if list1[i] == list2[j]:
            if i + j < mini:
                mini = i + j
            res[list1[i]] = i + j
            i += 1
            j = 0
        else:
            j += 1

        if j == len(list2):
            i += 1
            j = 0
    
    # return [r for r, s in res.items() if s == mini] 
    return list(map(lambda x: x[0], filter(lambda x: x[1] == mini, res.items())))


if __name__ == '__main__':
    strs1 = input().split(",")
    strs2 = input().split(",")

    print(findRestaurant(strs1, strs2))