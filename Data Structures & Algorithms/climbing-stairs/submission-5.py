class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)

        # def recursive(x):
        #     if dp[x] != -1:
        #         return dp[x]
        #     if x in [1,2]: 
        #         return x
        #     dp[x] = recursive(x-1) + recursive(x-2)
        #     return dp[x]

        # return recursive(n)
        if n in [1, 2]:
            return n

        # dp[1], dp[2] = 1, 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        prev = 2
        db_prev = 1
        for i in range(3, n):
            tmp = prev
            prev = prev + db_prev
            db_prev = tmp
        return prev + db_prev


        