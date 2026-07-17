class Solution:
    def recursive(self, n, cost, dp):
        """return the min cost to reach index n"""
        if dp[n] != -1:
            return dp[n]
        if n == 0 or n == 1:
            dp[n] = 0
            return 0
        dp[n] = min(self.recursive(n-1, cost, dp)+cost[n-1], self.recursive(n-2, cost, dp)+cost[n-2])
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n+1)
        dp[n] = self.recursive(n, cost, dp)
        return dp[n]

        