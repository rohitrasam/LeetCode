# https://leetcode.com/problems/destination-city/description/?envType=problem-list-v2&envId=hash-table


from typing import List


def destCity(paths: List[List[str]]) -> str:
    # link = {}
    # for sor, dest in paths:
    #     link[sor] = dest

    # for sor in link:
    #     if link[sor] not in link:
    #         return link[sor]

    paths = dict(paths)

    for dest in paths.values():
        if dest not in paths:
            return dest
    


if __name__ == '__main__':
    case = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(destCity(case))
    case = [["B","C"],["D","B"],["C","A"]]
    print(destCity(case))
    case = [["A","Z"]]
    print(destCity(case))