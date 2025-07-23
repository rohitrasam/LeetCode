# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=problem-list-v2&envId=tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(node: TreeNode, prev: str) -> None:
            if not node.left and not node.right:
                nonlocal total
                total += int(prev)
                return
            
            if node.left:
                dfs(node.left, prev+str(node.left.val))
            if node.right:
                dfs(node.right, prev+str(node.right.val))

        dfs(root, str(root.val))
        return total
    

tt = TreeNode(4)
tt.left = TreeNode(9)
tt.left.left = TreeNode(5)
tt.left.right = TreeNode(1)
tt.right = TreeNode(0)

s = Solution()
print(s.sumNumbers(tt))