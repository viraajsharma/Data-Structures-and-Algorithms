# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        arr = []
        if (root !=None):
            arr.append(root.val)
            left = self.preorderTraversal(root.left)
            right = self.preorderTraversal(root.right)
            return arr + left +right
        else :
            return []