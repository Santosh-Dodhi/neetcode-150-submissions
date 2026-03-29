class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = set()
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_ele = tuple(sorted([nums[i], nums[j], nums[k]]))
                        if sorted_ele not in s:
                            s.add(sorted_ele)
        
        s = list(s) 
        s = [list(ele) for ele in s]
        return s