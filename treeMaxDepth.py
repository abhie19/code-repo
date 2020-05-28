# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        s = []
        depth = 0
        s.append((1, root))
        while s:
            cur_depth, node = s.pop()
            if node is not None:
                depth = max(depth, cur_depth)
                s.append((cur_depth+1, node.left))
                s.append((cur_depth+1, node.right))
        return depth
        # Bottom Up
        # return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
