class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """n^2 approach: run nested for loop:"""
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        """n*log(n) approach: sort and compare with prev."""
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False

        """o(n) approach but with o(n) space complexity"""
        y = set(nums)
        return not len(nums) == len(y)

        