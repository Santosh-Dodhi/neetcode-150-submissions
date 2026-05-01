class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        #  a ^ a = 0 and a ^ 0 = a where ^ is bitwise xor operator
        for ele in nums:
            xor = xor ^ ele
        return xor