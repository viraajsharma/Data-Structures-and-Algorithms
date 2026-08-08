# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
            prev = None
            minimum = float("inf")

            def inorder(node):
                nonlocal prev, minimum
                if node is None:
                    return
                inorder(node.left)
                if prev != None:
                    diff = node.val - prev
                    if diff<minimum:
                        minimum = diff
                prev = node.val
                inorder(node.right)
            inorder(root)
            return minimum
        
        