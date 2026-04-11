class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        time: O(logn)
        space: O(1)
        approach: nums[mid] <= nums[end] --> search in [st, mid]
                  nums[mid] > nums[end] --> search in [mid+1, end]
        """
        n = len(nums)
        st, end = 0, n-1
        while st < end:
            mid = st + (end-st)//2
            if nums[mid] > nums[end]:
                st = mid + 1
            else:
                end = mid # IMP: including mid it can be minEle
        return nums[end]