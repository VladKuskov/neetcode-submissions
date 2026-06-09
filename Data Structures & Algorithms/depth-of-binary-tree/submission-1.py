# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        # go through all right nodes first, then left nodes.
        right_depth = self.maxDepth(root.right)
        left_depth = self.maxDepth(root.left)
        # increments by +1 each iteration of a branch
        max_depth = max(right_depth, left_depth) + 1
        return max_depth
        