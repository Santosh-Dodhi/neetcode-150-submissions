class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        time: o(n^2)
        space: o(n) for result + o(1) extra
        """
        # n = len(nums)
        # ans = [1] * n
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if j == i:
        #             continue
        #         prod *= nums[j]
        #     ans[i] = prod
        # return ans


        """
        time: o(n)
        space: o(n) for result
        """
        n = len(nums)
        num_zeros = nums.count(0)
        if num_zeros >= 2:
            return [0]*n
        elif num_zeros == 1:
            ans = [0] * n
            idx = nums.index(0)
            prod = 1
            for i in range(idx):
                prod *= nums[i]
            for i in range(idx+1, n):
                prod *= nums[i]
            ans[idx] = prod
            return ans
        else: # NO Zeros
            prod = 1
            for ele in nums:
                prod *= ele
            ans = [1] * n
            for i in range(n):
                ans[i] = prod // nums[i]
            return ans


                
        