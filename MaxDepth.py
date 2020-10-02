# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    # bottom up
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_d = 0
        left_d = self.maxDepth(root.left) + 1
        right_d = self.maxDepth(root.right) + 1
        return max(left_d, right_d)
    """
    # top down
    def maxDepth(self, root: TreeNode) -> int:
        
        def maxD(root, depth):
            # leaf node
            if root.left is None and root.right is None:
                return max(depth, self.max_d)
            l_d = maxD(root.left, depth + 1)
            r_d = maxD(root.right, depth + 1)
            self.max_d = max(l_d, r_d)
            return self.max_d + 1
            
        if root is None:
            return        
        self.max_d, self.curr_d = 0, 0
        maxD(root, self.curr_d)
        return self.max_d
