class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # easiest way to keep a dictionary with value: key and check whenever we find the difference of target - current
        temp_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in temp_dict:
                return [i,temp_dict[target-nums[i]]]
            else:
                temp_dict[nums[i]] = i
