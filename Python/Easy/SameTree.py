from BinaryTreeInorder import TreeNode


def isSameTree(p: TreeNode, q: TreeNode):

    """ Solution 1 """
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


    """ My Solution """

    # if not p and not q:
    #     return True

    # p_list = [p]
    # q_list = [q]

    # while p_list or q_list:

    #     p_curr = p_list.pop(0)
    #     q_curr = q_list.pop(0)

    #     if (p_curr and q_curr) and (p_curr.val == q_curr.val):

    #         if p_curr.left or q_curr.left:
    #             p_list.append(p_curr.left)
    #             q_list.append(q_curr.left)

    #         if p_curr.right or q_curr.right:
    #             p_list.append(p_curr.right)
    #             q_list.append(q_curr.right)
    #     else:
    #         return False
    
    # return True
    
if __name__ == '__main__':

    bt_p = TreeNode(1)
    bt_p.left = TreeNode(1)
    bt_p.right = TreeNode(2)

    bt_q = TreeNode(1)
    bt_q.left = TreeNode(2)
    bt_q.right = TreeNode(1)
    
print(isSameTree(None, None))
