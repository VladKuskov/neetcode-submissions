# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def depth_helper(node):
            if node is None:
                return 0
            left = depth_helper(node.left)
            right = depth_helper(node.right)
            self.best = max(self.best, left + right)
            return 1 + max(left, right)

        depth_helper(root)
        return self.best
