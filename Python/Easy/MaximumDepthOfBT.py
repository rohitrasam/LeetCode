from BinaryTreeInorder import TreeNode

def maxDepth(root: TreeNode) -> int:
    
    return 0 if not root else 1 + max(maxDepth(root.left), maxDepth(root.right))



if __name__ == '__main__':
    bt = TreeNode(3)
    bt.left = TreeNode(9)
    bt.right = TreeNode(20)
    bt.left.left = TreeNode(3)
    bt.left.right = TreeNode(3)
    bt.right.left = TreeNode(15)
    bt.right.right = TreeNode(7)
    bt.right.right.left = TreeNode(2)
    bt.right.right.right = TreeNode(45)
    print(maxDepth(bt))