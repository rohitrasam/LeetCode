# https://leetcode.com/problems/smallest-string-starting-from-leaf/description/?envType=problem-list-v2&envId=backtracking
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    small = "z" * 14
    a = ord("a")

    def dfs(node: TreeNode, curr: str) -> None:
        if not node.left and not node.right:
            nonlocal small
            small = min(small, curr)
            return

        if node.left:
            dfs(node.left, chr(node.left.val + a) + curr)
        if node.right:
            dfs(node.right, chr(node.right.val + a) + curr)

    dfs(root, chr(root.val + a))
    return small


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)

    print(smallestFromLeaf(root))
