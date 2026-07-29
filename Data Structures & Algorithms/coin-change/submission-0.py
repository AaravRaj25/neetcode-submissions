class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,len(dp)):
            for n in coins:
                if (i-n) < 0:
                    continue
                else:
                    dp[i] = min(dp[i] , 1 + dp[i-n])
        return dp[-1] if dp[-1] != float('inf') else -1
        

        