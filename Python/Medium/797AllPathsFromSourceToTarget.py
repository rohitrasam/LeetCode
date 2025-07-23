# https://leetcode.com/problems/all-paths-from-source-to-target/description/?envType=problem-list-v2&envId=backtracking


from typing import Dict, List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    dest = len(graph) - 1
    paths: List[List[int]] = []
    adj: Dict[int, List[int]] = {}

    for node, ne in enumerate(graph):
        adj[node] = ne

    def dfs(node: int, path: List[int]) -> None:
        if node == dest:
            paths.append(path[:])
            return

        for n in adj[node]:
            path.append(n)
            dfs(n, path)
            path.pop()

    dfs(0, [0])
    return paths


if __name__ == "__main__":
    case = [[1, 2], [3], [3], []]
    print(allPathsSourceTarget(case))
    case = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    print(allPathsSourceTarget(case))
