class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] > prices[i]:
                    ans = max(ans, prices[j] - prices[i])
        return ans
        