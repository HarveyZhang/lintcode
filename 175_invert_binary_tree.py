"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        if not root:
            return root

        tmp_node = root.left
        root.left = root.right
        root.right = tmp_node

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)
