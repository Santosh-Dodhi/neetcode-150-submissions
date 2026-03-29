class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max_heights = [0] * n
        right_max_heights = [0] * n
        left_max = right_max = 0
        for i in range(1, n):
            left_max = max(left_max, height[i-1])
            left_max_heights[i] = left_max

        print(left_max_heights)

        for i in range(n-2, -1, -1):
            right_max = max(right_max, height[i+1])
            right_max_heights[i] = right_max

        print(right_max_heights)

        ans = 0
        for i in range(n):
            ans += max(0, min(left_max_heights[i], right_max_heights[i]) - height[i])
        
        return ans
        