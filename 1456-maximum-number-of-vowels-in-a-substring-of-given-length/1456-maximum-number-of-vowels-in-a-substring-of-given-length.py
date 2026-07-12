class Solution(object):
    def maxVowels(self, s, k):
        vowels = {'a','e','i','o','u'}
        count = 0
        for ch in s[0:k]:
            if ch in vowels:
                count +=1
        max_count = count

        for i in range(k,len(s)):
            if s[i-k] in vowels:
                count -=1
            if s[i] in vowels:
                count +=1
            max_count = max(max_count, count)
        return max_count

                
