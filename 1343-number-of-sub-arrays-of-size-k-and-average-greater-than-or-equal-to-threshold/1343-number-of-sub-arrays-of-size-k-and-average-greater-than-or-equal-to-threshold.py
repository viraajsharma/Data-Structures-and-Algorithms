class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        window_1_sum = sum(arr[0:k])
        count =0
        current_sum = window_1_sum
        if current_sum >= threshold*k:
            count += 1
        for i in range(k,len(arr)):
            left,right = arr[i-k],arr[i]
            current_sum = current_sum - left + right
            if current_sum >= threshold*k:
                count +=1
        return count