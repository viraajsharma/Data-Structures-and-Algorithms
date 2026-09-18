class Solution(object):
    def threeSum(self, nums):
        result = []

        for i in range(len(nums)):
            seen = set()
            target = -nums[i]

            for j in range(i + 1, len(nums)):
                needed = target - nums[j]

                if needed in seen:
                    triplet = [nums[i], needed, nums[j]]
                    triplet.sort()

                    if triplet not in result:
                        result.append(triplet)

                seen.add(nums[j])
        return result