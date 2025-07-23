# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/?envType=problem-list-v2&envId=hash-table



from typing import Dict, List


def groupThePeople(groupSizes: List[int]) -> List[List[int]]:
    """ My Solution """
    # groups: Dict[int, List[int]] = {}
    # ans: List[List[int]] = []
    # for person, size in enumerate(groupSizes):
    #     if size in groups and len(groups[size]) < size:
    #         groups[size].append(person)
    #         if len(groups[size]) == size:
    #             ans.append(groups[size])
    #             groups[size] = []
    #     else:
    #         groups[size] = [person]
    #         if size == 1:
    #             ans.append(groups[1])
    #             groups[1] = []
    # return ans

    """ Leetcode solution """
    groups: Dict[int, List[int]] = {}
    ans: List[List[int]] = []

    for person, size in enumerate(groupSizes):
        if size not in groups:
            groups[size] = []
        groups[size].append(person)

        if len(groups[size]) == size:
            ans.append(groups[size])
            groups[size] = []
    
    return ans
        

if __name__ == '__main__':

    case = [3,3,3,3,3,1,3]
    print(groupThePeople(case))
    case = [2,1,3,3,3,2]
    print(groupThePeople(case))
    case = [3,4,3,3,4,4,3,4,3,3]
    print(groupThePeople(case))
