class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Brute force
        
        """if len(s)==0: return True
        for i in range(1,len(s)+1):
            if not s[:i] in wordDict: continue
            if self.wordBreak(s[i:], wordDict):
                return True
        return False
        """
        # Dynamic Programming with Memoization
        dp = [False] * (len(s)+1) # create the dp array to store intermediate results
        dp[0] = True
        # divide into subproblem by parsing the string 
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True # if the subproblem satisfies, mark ith position as True
                    break
        return dp[-1] # check t˙e dp value at len(s) or end of dp array
