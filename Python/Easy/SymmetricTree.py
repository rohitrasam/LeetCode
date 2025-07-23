from BinaryTreeInorder import TreeNode


"""Recursion solution"""

# lvl = 0

# def isEqual(left:TreeNode, right: TreeNode) -> bool:
#     if not left and not right:
#         return True  
#     elif not left or not right:
#         return False
    
#     global lvl
#     lvl += 1
#     print(lvl, left.val, right.val)
#     return left.val == right.val and isEqual(left.left, right.right) and isEqual(left.right, right.left)

# def isSymmetric(root: TreeNode) -> bool:

#     return isEqual(root.left, root.right)
    

"""Iterative solution"""    

def isSymmetric(root: TreeNode) -> bool:
        if not root:
            return False
    
        left = [root.left]
        right = [root.right]
        while left and right:
            curr_left = left.pop(0)
            curr_right = right.pop(0)
            
            if not curr_left and not curr_right:
                return True
            
            if (not curr_left or not curr_right) or curr_left.val != curr_right.val:
                return False

            if curr_left.left and curr_right.right:
                left.append(curr_left.left)
                right.append(curr_right.right)
            elif curr_left.left or curr_right.right:
                return False

            if curr_left.right and curr_right.left:
                left.append(curr_left.right)
                right.append(curr_right.left)
            elif curr_left.right or curr_right.left:
                return False
                
        return True


if __name__ == '__main__':

    bt = TreeNode(1)
    bt.left = TreeNode(2)
    bt.right = TreeNode(2)
    # bt.left.left = TreeNode(3)
    bt.left.right = TreeNode(3)
    # bt.right.left = TreeNode(4)
    bt.right.right = TreeNode(3)
    print(isSymmetric(bt))

