class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        time: O(n^2)
        space: O(1)
        """
        # n = len(heights)
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         ans = max(ans, (j-i)*(min(heights[i], heights[j])))
        # return ans

        """
        time: O(n)
        space: O(1)
        """
        n = len(heights)
        i = 0
        j = n - 1
        ans = 0
        while i < j:
            ans = max(ans, min(heights[i], heights[j])*(j-i))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return ans


