# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/?envType=problem-list-v2&envId=dynamic-programming


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: Optional[TreeNode]) -> int:

    res = [root.val]

    def dfs(root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        leftMax = dfs(root.left)
        rightMax = dfs(root.right)

        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        res[0] = max(root.val + leftMax + rightMax, res[0])

        return root.val + max(leftMax, rightMax)

    dfs(root)
    return res[0]



if __name__ == '__main__':
    pass