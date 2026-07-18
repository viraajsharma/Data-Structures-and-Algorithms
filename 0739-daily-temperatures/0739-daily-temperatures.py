class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        answer = [0]*len(temperatures)
        for i in range(len(temperatures)):
                while len(stack)>0 and temperatures[i]> temperatures[stack[-1]]:
                    idx = stack.pop()
                    answer[idx] = i - idx
                stack.append(i)
        return answer
