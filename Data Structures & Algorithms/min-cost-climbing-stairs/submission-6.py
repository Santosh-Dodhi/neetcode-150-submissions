class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        #state: dp[i] store the min cost to reach the index i
        # dp = [-1]*(n+1)
        # dp[0] = dp[1] = 0
        # for i in range(2, n+1):
        #     dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        # return dp[n]

        st0 = st1 = 0 
        for i in range(2, n+1):
            c = min(st0+cost[i-2] , st1+cost[i-1])
            st0 = st1
            st1 = c
        return c

        