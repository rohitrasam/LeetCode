# https://leetcode.com/problems/most-frequent-subtree-sum/description/?envType=problem-list-v2&envId=tree


from collections import defaultdict
from typing import DefaultDict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findFrequentTreeSum(root: Optional[TreeNode]) -> List[int]:
    # sum_count: DefaultDict = defaultdict(int)
    # total: int = 0

    # def dfs(curr: Optional[TreeNode]) -> None:
    #     nonlocal total
    #     total += curr.val

    #     if curr.left:
    #         dfs(curr.left)

    #     if curr.right:
    #         dfs(curr.right)

    # queue: List[TreeNode] = [root]

    # while queue:
    #     curr_node = queue.pop()

    #     dfs(curr_node)

    #     sum_count[total] += 1
    #     total = 0

    #     if curr_node.left:
    #         queue.append(curr_node.left)
    #     if curr_node.right:
    #         queue.append(curr_node.right)

    # max_sum = max(sum_count.values())
    # res = list(map(lambda x: x[0], filter(lambda x: x[1] == max_sum, sum_count.items())))
    # return res

    sum_count: DefaultDict = defaultdict(int)

    def dfs(curr: Optional[TreeNode]) -> int:
        if not curr:
            return 0

        left = dfs(curr.left)
        right = dfs(curr.right)

        total = curr.val + left + right
        sum_count[total] += 1

        return total

    dfs(root)

    max_val = max(sum_count.values())

    return list(
        map(lambda x: x[0], filter(lambda x: x[1] == max_val, sum_count.items()))
    )


if __name__ == "__main__":
    case1 = TreeNode(5)
    case1.left = TreeNode(2)
    case1.right = TreeNode(-3)

    case2 = TreeNode(5)
    case2.left = TreeNode(2)
    case2.right = TreeNode(-5)

    case3 = TreeNode(5)
    case3.left = TreeNode(2)
    case3.right = TreeNode(-5)
    case3.left.right = TreeNode(4)
    case3.right.left = TreeNode(3)
    case3.right.right = TreeNode(5)

    print(findFrequentTreeSum(case1))
    print(findFrequentTreeSum(case2))
    print(findFrequentTreeSum(case3))
