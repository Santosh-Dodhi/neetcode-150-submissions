class Solution:
    def recursive(self, i, nums, dp):
        if i < 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        if i == 0:
            dp[i] = nums[0]
            return nums[0]
        dp[i] = max(self.recursive(i-2, nums, dp)+ nums[i], self.recursive(i-1, nums, dp))
        return dp[i]
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # state: dp[i] store the max value for array of len i
        dp = [-1]*(n+1)
        return self.recursive(n-1, nums, dp)
        