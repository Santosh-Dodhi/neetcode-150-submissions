class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        for i in range(n):
            left = i
            while left-1 >= 0 and heights[left-1] >= heights[i]:
                left -= 1
            
            right = i
            while right+1 < n and heights[right+1] >= heights[i]:
                right += 1

            area = max(area, (right-left+1)*heights[i])
        return area