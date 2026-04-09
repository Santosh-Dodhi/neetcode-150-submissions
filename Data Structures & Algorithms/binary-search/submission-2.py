class Solution:
    def binary_search(self, st, end, nums, target):
        if st > end:
            return -1
        mid = st + (end-st) // 2
        print(f"{mid=}")
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(mid+1, end, nums, target)
        else:
            return self.binary_search(st, mid-1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        st, end = 0, len(nums)-1
        return self.binary_search(st, end, nums, target)
        