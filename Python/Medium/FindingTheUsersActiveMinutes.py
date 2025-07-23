# https://leetcode.com/problems/finding-the-users-active-minutes/?envType=problem-list-v2&envId=hash-table

from typing import Dict, List, Set


def findingUsersActiveMinutes(logs: List[List[int]], k: int) -> List[int]:
    
    ans = [0] * k
    log_count: Dict[int, Set] = {}

    for uid, time in logs:
        if uid in log_count:
            log_count[uid].add(time)
        else:
            log_count[uid] = {time}
    
    for uid in log_count:
        uam = len(log_count[uid])
        ans[uam-1] += 1
    
    return ans


if __name__ == '__main__':
    case = [[0,5],[1,2],[0,2],[0,5],[1,3]], 5
    print(findingUsersActiveMinutes(*case))
    case = [[1,1],[2,2],[2,3]], 4
    print(findingUsersActiveMinutes(*case))
    case = [[0,6],[1,5],[0,5],[1,4],[2,6],[2,7]], 7
    print(findingUsersActiveMinutes(*case))