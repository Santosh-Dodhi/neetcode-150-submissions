class Solution:
    """
    time: O(logm + logn)
    space: O(m)
    approach: 2 binary pass with providing col0
    """
    # def lowerBound(self, nums, target):
    #     st, end = 0, len(nums)-1
    #     while st <= end:
    #         mid = st + (end-st)//2
    #         if nums[mid] >= target:
    #             end = mid - 1
    #         else:
    #             st = mid + 1
    #     return end

    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     col0 = []
    #     m, n = len(matrix), len(matrix[0])
    #     for row in matrix:
    #         col0.append(row[0])
    #     print(col0)
    #     idx = self.lowerBound(col0, target)
    #     if idx+1 < m and col0[idx+1] == target:
    #         return True
    #     print(idx)
    #     if idx >= 0:
    #         lower = self.lowerBound(matrix[idx], target)
    #         if lower+1 < n and matrix[idx][lower+1] == target:
    #             return True
    #     return False

    """
    time: O(logm + logn)
    space: O(m)
    approach: 2 binary pass with providing col0
    """
    def lowerBound(self, matrix, target, idx, which="row"):
        if which == "col":
            st, end = 0, len(matrix)-1
            while st <= end:
                mid = st + (end-st)//2
                if matrix[mid][idx] >= target:
                    end = mid - 1
                else:
                    st = mid + 1
            return end
        else:
            st, end = 0, len(matrix[0])-1 
            while st <= end:
                mid = st + (end-st)//2
                if matrix[idx][mid] >= target:
                    end = mid - 1
                else:
                    st = mid + 1
            return end


        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col0 = []
        m, n = len(matrix), len(matrix[0])
        idx = self.lowerBound(matrix, target, 0, "col")
        if idx+1 < m and matrix[idx+1][0] == target:
            return True
        print(idx)
        if idx >= 0:
            lower = self.lowerBound(matrix, target, idx, "row")
            if lower+1 < n and matrix[idx][lower+1] == target:
                return True
        return False

    


        