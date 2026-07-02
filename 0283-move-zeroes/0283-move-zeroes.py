class Solution(object):
    def moveZeroes(self, nums):
        left = 0 
        right = 0 
        for right in range(0,len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left = left+1
            else:
                right = right +1
        for left in range(left,len(nums)):
            nums[left] = 0