class Solution(object):
    def backspaceCompare(self, s, t):
        stack_s = []
        stack_t = []
        for i in range(len(s)):
            if s[i] == "#":
                if len(stack_s) >0:
                    stack_s.pop()
                else:
                    continue
            else:
                stack_s.append(s[i])

        for j in range(len(t)):
            if t[j] == "#":
                if len(stack_t) >0:
                    stack_t.pop()
                else:
                    continue
            else:
                stack_t.append(t[j])
        if stack_s == stack_t:
            return True
        else:
            return False