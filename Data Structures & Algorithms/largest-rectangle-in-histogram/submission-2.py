class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        time: O(n^3)
        space: O(n)
        approach: nested loops (brute force) (TLE)
        """
        # n = len(heights)
        # area = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         area = max(area, (j-i+1)*min(heights[i:j+1]))
        #         print(area)
        # return area

        """
        time: O(n^2)
        space: O(n)
        approach: nested loops (brute force) (TLE)
        """
        n = len(heights)
        area = 0
        for i in range(n):
            min_ele = heights[i]
            for j in range(i, n):
                if heights[j] < min_ele:
                    min_ele = heights[j]
                area = max(area, (j-i+1)*min_ele)
        return area
        

        