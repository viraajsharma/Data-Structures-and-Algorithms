class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum = sum(nums[0:k])
        best_sum =  current_sum
        for i in range(k,len(nums)):
            left = nums[i-k]
            right = nums[i]
            current_sum = current_sum - left +right
            if current_sum>best_sum:
                best_sum = current_sum
        return float(best_sum)/k
        