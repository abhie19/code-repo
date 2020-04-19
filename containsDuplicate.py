def c(self, nums: List[int]) -> bool:
    seen = set()
    if len(nums) == 0: return False
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
