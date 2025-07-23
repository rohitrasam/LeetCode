

class TreeNode:

    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        

def inorder(rootNode: TreeNode):
    """ Solution 1 """
    # return inorder(rootNode.left) + [rootNode.val] + inorder(rootNode.right) if rootNode else []
    
    """ My solution """
    curr = rootNode
    visited = [curr]
    curr = curr.left
    ans = []
    while curr or visited:
        if curr:
            visited.append(curr)
            curr = curr.left
        else:
            curr = visited.pop(-1)
            ans.append(curr.val)
            curr = curr.right

    print(ans)

if __name__ == '__main__':

    bt = TreeNode(1)
    bt.left = TreeNode(2)
    # bt.right.left = TreeNode(3)

    bt.right = TreeNode(3)
    bt.left.left = TreeNode(4)
    bt.left.right = TreeNode(5)

    bt.right.right = TreeNode(6)
    bt.right.left = TreeNode(7)
    print(inorder(bt))
