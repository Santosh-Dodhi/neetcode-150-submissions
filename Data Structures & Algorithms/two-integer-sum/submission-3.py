class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = {}
        for i, ele in enumerate(nums):
            if target - ele in mydic:
                return [mydic[target-ele], i]
            else:
                mydic[ele] = i
