class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        time: O(n^2)
        space: O(1)"""
        # ans = 0
        # n = len(prices)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if prices[j] > prices[i]:
        #             ans = max(ans, prices[j] - prices[i])
        # return ans
        

        """
        time: O(n)
        space: O(n)
        """
        # profit = 0
        # n = len(prices)
        # buy_prices = [float('inf')] * n
        # for i in range(1, n):
        #     buy_prices[i] = min(buy_prices[i-1], prices[i-1])
        # # print(buy_prices)

        # for i in range(n):
        #     if prices[i] - buy_prices[i] > profit:
        #         profit = prices[i] - buy_prices[i]
        # return profit

        """
        time: O(n)
        space: O(1)
        approach: for loop
        """
        # n = len(prices)
        # profit = 0
        # min_buy = prices[0]
        # for i in range(1, n):
        #     profit = max(profit, prices[i]-min_buy)
        #     min_buy = min(min_buy, prices[i])
        # return profit

        """
        time: O(n)
        space: O(1)
        approach: 2-pointers
        """
        n = len(prices)
        l = 0
        r = 1
        profit = 0
        while r < n:
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                profit = max(profit, prices[r]-prices[l])
                r += 1
        return profit
        

            