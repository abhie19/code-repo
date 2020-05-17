class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        # binary search based on ordered array hint
        # start with a mid point

        while start <= end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                # normal ascending window
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > nums[mid] and target <= nums[end]:
                    # right window
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
