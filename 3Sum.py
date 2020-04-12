class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out_list = []
        if len(nums)<3: return []
        nums = sorted(nums)
        len_nums = len(nums)
        for i in range(len_nums-2):
            curr = nums[i]
            if i>0 and nums[i-1]==nums[i]: continue
            l,r = i+1, len_nums-1
            while l<r:
                s = curr+nums[l]+nums[r]
                if s == 0:
                    out_list.append([curr,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                    while nums[r] == nums[r+1] and l<r:
                        r-=1
                elif s<0:
                    l += 1
                else:
                    r -= 1

        return out_list
