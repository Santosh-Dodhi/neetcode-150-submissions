class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        time: O(n^3)
        space: O(n)
        """
        # n = len(nums)
        # s = set()
        # for i in range(0, n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 sorted_ele = tuple(sorted([nums[i], nums[j], nums[k]]))
        #                 if sorted_ele not in s:
        #                     s.add(sorted_ele)
        
        # s = list(s) 
        # s = [list(ele) for ele in s]
        # return s

        """
        time: 
        space: 
        """
        ans = set()

        def two_sum(arr, target):
            s = set()
            for ele in arr:
                if target-ele in s:
                    ans.add(tuple(sorted([target-ele, ele, -target])))   
                else:
                    s.add(ele)

        n = len(nums)
        for i in range(n):
            target = -nums[i]
            two_sum(nums[:i] + nums[i+1:], target)
        return [list(ele) for ele in ans]
