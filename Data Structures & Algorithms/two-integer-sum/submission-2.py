class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """o(n^2) time complexity: find among all possible pairs"""
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [i, j]
        
        """o(nlog(n)) time complexity: sort + st and end pointers"""
        """The following soln will not work because we need to return index"""
        # nums = sorted(nums)

        # st = 0
        # end = len(nums) - 1
        # while st < end:
        #     if nums[st] + nums[end] > target:
        #         end -= 1
        #     elif nums[st] + nums[end] < target:
        #         st += 1
        #     else:
        #         return [st, end]

        """o(n) time and space complexity"""
        mydic = {}
        for i, ele in enumerate(nums):
            if target - ele in mydic:
                return [mydic[target-ele] , i]
            else:
                mydic[ele] = i
        




