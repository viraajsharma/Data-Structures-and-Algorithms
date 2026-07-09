class Solution(object):
    def isSubsequence(self, s, t):
        left = 0
        right = 0
        if len(s) == 0:
            return True
        while right < len(t):
            if s[left] == t[right]:
                left = left +1
                right = right +1
            else:
                right = right+1
            if left == len(s):
                return True
        return False
            

            


        