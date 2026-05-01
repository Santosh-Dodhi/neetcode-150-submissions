class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        #  a ^ a is 0
        for ele in nums:
            xor = xor ^ ele
        return xor