class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        n = len(nums)
        ans = 1
        if n == 0: return 0
        if n == 1: return 1
        i = 1
        while i < n:
            count = 1
            while i < n and nums[i] == (nums[i-1] + 1):
                count += 1
                print(i,nums[i], count)
                i += 1
            ans = max(ans, count)
            i += 1

        return ans

                

        