# https://leetcode.com/problems/redundant-connection/description/

from collections import defaultdict
from typing import DefaultDict, Dict, List


class UnionFind:
    def __init__(self, n: int):
        self.parent: Dict[int, int] = {i: i for i in range(1, n + 1)}
        self.rank: DefaultDict[int, int] = defaultdict(lambda: 1)

    def find(self, node: int) -> int:
        while self.parent[node] != node:
            node = self.parent[node]
        return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        p1 = self.find(node1)
        p2 = self.find(node2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True


def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    uf = UnionFind(len(edges))

    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]

    return []


if __name__ == "__main__":
    case = [[1, 2], [1, 3], [2, 3]]
    print(findRedundantConnection(case))
    case = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(findRedundantConnection(case))
    case = [[1, 2], [2, 3], [3, 4], [4, 6], [1, 5], [5, 6]]
    print(findRedundantConnection(case))
