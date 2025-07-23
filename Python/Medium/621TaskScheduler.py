# https://leetcode.com/problems/task-scheduler/

from collections import Counter, defaultdict, deque
import heapq
from typing import Deque, List, Tuple


def leastInterval(tasks: List[str], n: int) -> int:
    """ Approach 1: Using Priority Q / Max Heap """

    # freq = [0] * 26
    # A = ord("A")
    # for task in tasks:
    #     freq[ord(task) - A] += 1
    
    # pq = [-f for f in freq if f > 0]
    # heapq.heapify(pq)

    # time = 0
    # while pq:

    #     cycle = n + 1
    #     store = []
    #     taskCount = 0

    #     while cycle > 0 and pq:
    #         current_freq = -heapq.heappop(pq)
    #         if current_freq > 1:
    #             store.append(-(current_freq-1))
    #         taskCount += 1
    #         cycle -= 1

    #     for x in store:
    #         heapq.heappush(pq, x)

    #     time += taskCount if not pq else n + 1

    # return time


    """ Approach 4: Using Math Formula """

    # freq = [0] * 26
    # maxCount = 0

    # for task in tasks:
    #     idx = ord(task) - ord('A')
    #     freq[idx] += 1
    #     maxCount = max(maxCount, freq[idx])
    
    # time = (maxCount - 1) * (n + 1)
    # for f in freq:
    #     if f == maxCount:
    #         time += 1

    # return max(len(tasks), time)

    # freq = defaultdict(int)
    # maxCount = 0

    # for task in tasks:
    #     freq[task] += 1
    #     maxCount = max(maxCount, freq[task])
    
    # time = (maxCount - 1) * (n + 1)
    # for f in freq.values():
    #     if f == maxCount:
    #         time += 1

    # return max(len(tasks), time)

    """ Neetcode Solution """
    

    count: Counter[str, int] = Counter(tasks)
    maxHeap: List[int] = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)
    
    time = 0
    q: Deque[Tuple[int]] = deque()

    while maxHeap or q:
        time += 1

        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append((cnt, time + n))

        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])

    return time




if __name__ == '__main__':
    case = ["A","A","A","B","B","B"], 2
    print(leastInterval(*case))
    case = ["A","C","A","B","D","B"], 1
    print(leastInterval(*case))
    case = ["A","A","A", "B","B","B"], 3
    print(leastInterval(*case))
    case = ["A","A","A"], 3
    print(leastInterval(*case))