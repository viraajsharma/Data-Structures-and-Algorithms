class Solution(object):
    def isMiddleElementUnique(self, nums):
        middle= nums[len(nums)//2]
        middle_in = len(nums)//2
        while True:
            for i in range(0,middle_in):
                if nums[i] == middle:
                    return False
            for j in range(middle_in+1,len(nums)):
                if nums[j]== middle:
                    return False
            return True

        