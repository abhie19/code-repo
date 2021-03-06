def isHappy(n: int) -> bool:
    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n,10)
            total_sum += digit**2
        return total_sum

    seen = set()
    # the max a number can hit is either 1 or it can go in a cycle. Checking both conditions below
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1
    
"""
isHappy(19)
> true
"""
