class Solution:
    def lowerBound(self, nums, target):
        st, end = 0, len(nums)-1
        while st <= end:
            mid = st + (end-st)//2
            if nums[mid] >= target:
                end = mid - 1
            else:
                st = mid + 1
        return end

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col0 = []
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            col0.append(row[0])
        print(col0)
        idx = self.lowerBound(col0, target)
        if idx+1 < m and col0[idx+1] == target:
            return True
        print(idx)
        if idx >= 0:
            lower = self.lowerBound(matrix[idx], target)
            if lower+1 < n and matrix[idx][lower+1] == target:
                return True
        return False

    


        