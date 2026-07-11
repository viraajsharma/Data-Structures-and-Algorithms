class Solution(object):
    def isValid(self, s):
        stack =[]
        pairs = {
            ')' :'(',
            '}' :'{' ,
            ']' : '[',
       }
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                else :
                    if stack[-1] == pairs[ch]:
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False