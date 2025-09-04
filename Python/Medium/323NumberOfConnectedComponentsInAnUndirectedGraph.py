# https://neetcode.io/problems/count-connected-components?list=blind75

from collections import defaultdict, deque
from typing import DefaultDict, Deque, Dict, List, Set

""" My Soultion: Disjoint set/Union Find"""

# class UnionFind:

#     def __init__(self, n: int):
#         self.ds: Dict[int, int] = {i: i for i in range(n)}
#         self.rank: DefaultDict[int, int] = defaultdict(lambda: 1)

#     def find(self, node: int) -> int:
#         while self.ds[node] != node:
#             node = self.ds[node]
#         return self.ds[node]

#     def union(self, node1: int, node2: int) -> None:
#         p1 = self.find(node1)
#         p2 = self.find(node2)

#         if p1 == p2:
#             return False
#         if self.rank[p1] > self.rank[p2]:
#             self.ds[p2] = p1
#             self.rank[p1] += self.rank[p2]
#             return True
#         else:
#             self.ds[p1] = p2
#             self.rank[p2] += self.rank[p1]
#             return True

# def countComponents(n: int, edges: List[List[int]]) -> int:

#     res = n
#     ds = UnionFind(n)
#     for src, dest in edges:
#         if ds.union(src, dest):
#             res -= 1

#     return res

""" DFS """

# def countComponents(n: int, edges: List[List[int]]) -> int:

#     adj: DefaultDict[List[int]] = defaultdict(list)

#     for u, v in edges:
#         adj[u].append(v)
#         adj[v].append(u)

#     visited: List[int] = [False] * n

#     def dfs(node: int) -> None:
#         for nei in adj[node]:
#             if not visited[nei]:
#                 visited[nei] = True
#                 dfs(nei)

#     res = 0
#     for curr_node in range(n):
#         if not visited[curr_node]:
#             visited[curr_node] = True
#             dfs(curr_node)
#             res += 1

#     return res


def countComponents(n: int, edges: List[List[int]]) -> int:
    adj: DefaultDict[List[int]] = defaultdict(list)

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited: Set[int] = set()

    def bfs(node: int) -> None:
        q: Deque[int] = deque()
        q.append(node)

        while q:
            curr = q.popleft()
            for nei in adj[curr]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)

    res = 0
    for curr_node in range(n):
        if curr_node not in visited:
            visited.add(curr_node)
            bfs(curr_node)
            res += 1

    return res


if __name__ == "__main__":
    case = (
        100,
        [
            [6, 27],
            [83, 9],
            [10, 95],
            [48, 67],
            [5, 71],
            [18, 72],
            [7, 10],
            [92, 4],
            [68, 84],
            [6, 41],
            [82, 41],
            [18, 54],
            [0, 2],
            [1, 2],
            [8, 65],
            [47, 85],
            [39, 51],
            [13, 78],
            [77, 50],
            [70, 56],
            [5, 61],
            [26, 56],
            [18, 19],
            [35, 49],
            [79, 53],
            [40, 22],
            [8, 19],
            [60, 56],
            [48, 50],
            [20, 70],
            [35, 12],
            [99, 85],
            [12, 75],
            [2, 36],
            [36, 22],
            [21, 15],
            [98, 1],
            [34, 94],
            [25, 41],
            [65, 17],
            [1, 56],
            [43, 96],
            [74, 57],
            [19, 62],
            [62, 78],
            [50, 86],
            [46, 22],
            [10, 13],
            [47, 18],
            [20, 66],
            [83, 66],
            [51, 47],
            [23, 66],
            [87, 42],
            [25, 81],
            [60, 81],
            [25, 93],
            [35, 89],
            [65, 92],
            [87, 39],
            [12, 43],
            [75, 73],
            [28, 96],
            [47, 55],
            [18, 11],
            [29, 58],
            [78, 61],
            [62, 75],
            [60, 77],
            [13, 46],
            [97, 92],
            [4, 64],
            [91, 47],
            [58, 66],
            [72, 74],
            [28, 17],
            [29, 98],
            [53, 66],
            [37, 5],
            [38, 12],
            [44, 98],
            [24, 31],
            [68, 23],
            [86, 52],
            [79, 49],
            [32, 25],
            [90, 18],
            [16, 57],
            [60, 74],
            [81, 73],
            [26, 10],
            [54, 26],
            [57, 58],
            [46, 47],
            [66, 54],
            [52, 25],
            [62, 91],
            [6, 72],
            [81, 72],
            [50, 35],
            [59, 87],
            [21, 3],
            [70, 12],
            [48, 4],
            [9, 23],
            [52, 55],
            [43, 59],
            [49, 26],
            [25, 90],
            [52, 0],
            [55, 8],
            [7, 23],
            [97, 41],
            [0, 40],
            [69, 47],
            [73, 68],
            [10, 6],
            [47, 9],
            [64, 24],
            [95, 93],
            [79, 66],
            [77, 21],
            [80, 69],
            [85, 5],
            [24, 48],
            [74, 31],
            [80, 76],
            [81, 27],
            [71, 94],
            [47, 82],
            [3, 24],
            [66, 61],
            [52, 13],
            [18, 38],
            [1, 35],
            [32, 78],
            [7, 58],
            [26, 58],
            [64, 47],
            [60, 6],
            [62, 5],
            [5, 22],
            [60, 54],
            [49, 40],
            [11, 56],
            [19, 85],
            [65, 58],
            [88, 44],
            [86, 58],
        ],
    )
    print(countComponents(*case))
    case = 1, []
    print(countComponents(*case))
    case = 3, [[0, 1], [0, 2]]
    print(countComponents(*case))
    case = 6, [[0, 1], [1, 2], [2, 3], [4, 5]]
    print(countComponents(*case))
