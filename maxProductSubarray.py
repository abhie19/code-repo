class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # the idea is to carry the max positive and negative values and check against each n
        # to navigate the affect of negative sign
        _len = len(nums)
        max_pro = min_pro = ans = nums[0]
        
        for i in range(1, _len):
            cand = (nums[i], max_pro*nums[i], min_pro*nums[i])
            max_pro = max(cand)
            min_pro = min(cand)
            ans = max(ans, max_pro)
        
        return ans
