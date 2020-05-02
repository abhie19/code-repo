class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # via Greedy
        
        max_sum = nums[0]
        # calculate the max sum up to the current and compare that with current val
        for i, val in enumerate(nums):
            if i == 0:
                curr_sum = val
                continue
            curr_sum = max(curr_sum + val, val)
            max_sum = max(curr_sum, max_sum)
        return max_sum
        
