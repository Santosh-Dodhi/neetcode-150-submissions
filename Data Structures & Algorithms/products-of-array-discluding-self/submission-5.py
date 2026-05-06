class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count0 = nums.count(0)
        n = len(nums)
        if count0 > 1:
            return [0]*n
        elif count0 == 1:
            prod = 1
            ans = []
            for ele in nums:
                if ele == 0:
                    pass
                else:
                    prod *= ele
            for ele in nums:
                if ele == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
        else:
            prod = 1
            for ele in nums:
                prod *= ele
            ans = []
            for ele in nums:
                ans.append(prod//ele)
        return ans
