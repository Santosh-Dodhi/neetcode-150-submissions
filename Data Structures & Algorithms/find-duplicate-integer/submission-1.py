class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # mySet = set()
        # for ele in nums:
        #     if ele not in mySet:
        #         mySet.add(ele)
        #     else:
        #         return ele

        i = 0
        n = len(nums)
        while i < n:
            tmp = nums[i]
            if tmp == -1:
                return i
            nums[i] = -1
            i = tmp


        