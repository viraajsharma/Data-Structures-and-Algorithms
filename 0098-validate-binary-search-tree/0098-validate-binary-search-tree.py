# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        return self.validate(root,float("-inf"), float("inf"))

    def validate(self,node,low,high):
        if node is None:
            return True
        if node.val <= low or node.val >= high:
            return False
        return (self.validate(node.left,low,node.val) and self.validate(node.right ,node.val, high ))
        