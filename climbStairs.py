class Solution:
    def climbStairs(self, n: int) -> int:
        # it is a DP problem coz the bigger problem can be disintegrated into 
        # subproblems which can then be summed to get final answer.
        # Also can be memoized to store solutions to subproblems
        dp = [0]*(n+1)
        #if n == 1: return 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            if dp[i] == 0:
                dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
