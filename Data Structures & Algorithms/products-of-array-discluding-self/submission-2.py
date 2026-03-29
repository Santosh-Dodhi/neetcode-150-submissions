class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        time: o(n)
        space: o(n)for result + o(n + n) extra space for prefix
                and suffix sum
        """
        # n = len(nums)
        # prefix = [1] * n
        # suffix = [1] * n
        
        # for i in range(1, n):
        #     prefix[i] = prefix[i-1]* nums[i-1]
        # # print(prefix)
            
        # for i in range(n-2, -1, -1):
        #     suffix[i] = suffix[i+1] * nums[i+1]
        # # print(suffix)

        # ans = [1] * n
        # for i in range(n):
        #     ans[i] = prefix[i] * suffix[i]

        # return ans

        """
        time: o(n)
        space: o(n)res + o(1) extra
        """
        n = len(nums)
        res = [1]* n

        #store prefix prod in res
        for i in range(1, n):
            res[i] = res[i-1]* nums[i-1]
        
        print(res)
        suffix = 1
        #store suffix prod in res itself
        for i in range(n-2, -1, -1):
            suffix *= nums[i+1]
            res[i] *= suffix

        print(res)

        return res
        

         
        