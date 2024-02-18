class Solution:
    def minCoins(self, coins, M, V):
        # code here
        dp=[V+1] * (V+1)
        dp[0]=0
        
        for coin in coins:
            for i in range(coin, V+1):
                if i-coin>=0:
                    dp[i]=min(dp[i], dp[i-coin]+1)
        
        return dp[V] if dp[V]!=V+1 else -1
