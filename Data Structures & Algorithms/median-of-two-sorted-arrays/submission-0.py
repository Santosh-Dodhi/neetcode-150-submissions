class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if n < m:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        left_side = (m + n + 1) // 2 #including median in left for odd case
        st, end = 0, m #as we are searching for partition 
        while st <= end:
            mid = st + (end-st)//2
            cut1 = mid
            cut2 = left_side - cut1
            l1 = nums1[cut1-1] if cut1 > 0 else -float('inf')
            r1 = nums1[cut1] if cut1 < m else float('inf')
            l2 = nums2[cut2-1] if cut2 > 0 else -float('inf')
            r2 = nums2[cut2] if cut2 < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (m+n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 < r2:
                st = mid + 1
            else:
                end = mid - 1
        

        