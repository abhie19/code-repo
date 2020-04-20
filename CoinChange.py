def coinChange(self, coins: List[int], amount: int) -> int:
    # this problem is solved using bottom up Dynamic programming
    dp = [float('inf')] * (amount+1)
    dp[0] = 0
    for a in range(amount+1):
        for coin in coins:
            if a >= coin:
                dp[a] = min(dp[a], dp[a - coin]+1)
    return dp[a] if dp[a] != float('inf') else -1
