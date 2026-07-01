class Solution(object):
    def removeElement(self, nums, val):
        if nums == []:
            return 0 
        left = 0
        right = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left = left +1
        return left

                
        