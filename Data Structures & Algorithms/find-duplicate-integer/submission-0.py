class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mySet = set()
        for ele in nums:
            if ele not in mySet:
                mySet.add(ele)
            else:
                return ele
        