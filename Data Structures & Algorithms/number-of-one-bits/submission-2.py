class Solution:
    def hammingWeight(self, n: int) -> int:
        #binary = bin(n)[2:]
        #return binary.count('1')
        
        
        #ans = n & 1
        #for i in range(1, 33):
        #    ans += ((n >> i) & 1) 
        #return ans
        
        ans = 0
        while n:
            n = n & (n-1)
            ans += 1
        return ans
