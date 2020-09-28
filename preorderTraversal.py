# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        # Recursive Traversal
        
        def recurseFunc(root, outList):
            # basecase - something that happens at the end of loop and independently
            if not root:
                return
            # not base case recurse
            self.outList.append(root.val)
            recurseFunc(root.left, self.outList)
            recurseFunc(root.right, self.outList)
        self.outList = []
        recurseFunc(root, self.outList)
        return self.outList
        """
        # Iterative Traversal
        # None case
        if root is None:
            return
        
        stack, out = [root,],[]
        while stack:
            root = stack.pop()
            if root is not None: # stack is not empty
                out.append(root.val)
            if root.right is not None: # coz stack is LIFO, so left goest last
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return out
