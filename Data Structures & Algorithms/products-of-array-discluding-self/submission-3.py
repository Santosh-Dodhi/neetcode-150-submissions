class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(n):
            prod = 1
            for j in range(n):
                if j == i:
                    continue
                prod *= nums[j]
            ans[i] = prod
        return ans

                
        