class Solution:
    """
    time: O(logn)
    space: O(logn)
    approach: recursive
    """
    # def binary_search(self, st, end, nums, target):
    #     if st > end:
    #         return -1
    #     mid = st + (end-st) // 2
    #     print(f"{mid=}")
    #     if nums[mid] == target:
    #         return mid
    #     elif nums[mid] < target:
    #         return self.binary_search(mid+1, end, nums, target)
    #     else:
    #         return self.binary_search(st, mid-1, nums, target)

    # def search(self, nums: List[int], target: int) -> int:
    #     st, end = 0, len(nums)-1
    #     return self.binary_search(st, end, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        """
        time: O(logn)
        space: O(1)
        approach: iterative
        """
        n = len(nums)
        st, end = 0, n-1

        # while st <= end:
        #     mid = st + (end-st)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         st = mid + 1
        #     else:
        #         end = mid - 1
        # return -1

        while st <= end:
            mid = st + (end-st)//2
            if nums[mid] > target:
                end = mid - 1
            else:
                st = mid + 1

        if nums[end] == target:
            return end
        return -1