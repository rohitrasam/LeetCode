# https://leetcode.com/problems/task-scheduler-ii/


from collections import defaultdict
from typing import List


def taskSchedulerII(tasks: List[int], space: int) -> int:
    freq = defaultdict(int)
    day = 0
    for task in tasks:
        day += 1

        if day < freq[task]:
            day = freq[task]
        
        freq[task] = day + space + 1

    return day



if __name__ == '__main__':

    # case = [1,2,1,2,3,1], 3
    # print(taskSchedulerII(*case))
    case = [5,8,8,5], 2
    print(taskSchedulerII(*case))
