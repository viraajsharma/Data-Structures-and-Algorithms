class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) -1 
        result = [0]*len(nums)
        right_2 = len(result)-1
        while left <= right:
            if nums[left]**2 < nums[right]**2:
                result[right_2] = nums[right]**2
                right_2 = right_2-1
                right = right -1
            else:
                result[right_2] = nums[left]**2
                right_2 = right_2-1
                left = left+1
        return result

                

                
            
            
        