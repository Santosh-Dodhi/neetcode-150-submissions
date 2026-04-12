class Solution:
    def binary_search(self, st, end, nums, target):
        while st<=end:
            mid = st + (end-st)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                st = mid + 1
            else:
                end = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        # get deflection point by get min
        n = len(nums)
        st, end = 0, n-1
        while st < end:
            mid = st + (end-st)//2
            if nums[mid] > nums[end]:
                st = mid + 1
            else:
                end = mid
        print(end) # end or st both at same point (deflection point)
        min_ele_id = end

        #check if deflection point is min?
        # if nums[min_ele_id] == target:
        #     return min_ele_id

        # if the deflection point is at starting.
        if min_ele_id == 0:
            x = self.binary_search(st, n-1, nums, target)
            print(f"{x=}")
            return x

        #binary search first half
        st = 0
        flag1 = self.binary_search(st, min_ele_id-1, nums, target)
        
        if flag1 == -1:
            #binary search second half
            st = min_ele_id 
            end = n-1
            flag2 = self.binary_search(st, end, nums, target)

        if flag1 == -1 and flag2 == -1:
            return -1
        elif flag1 >= 0:
            return flag1
        else:
            return flag2
        


