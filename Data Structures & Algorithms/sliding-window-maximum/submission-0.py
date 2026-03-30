class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        i = 0
        j = k-1
        ans = []
        while j < n:
            ans.append(max(nums[i:j+1]))
            j += 1
            i += 1
        return ans


        