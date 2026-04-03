class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        time: O(n) + O(klogn)
        space: O(n)
        approach: heaps
        """
        # from collections import Counter
        # import heapq
        # counter = list(Counter(nums).items()) # O(n)
        # heap = [(-y, x) for x,y in counter] # O(n)

        # heapq.heapify(heap) # O(n)

        # ans = []
        # while k: # O(k)
        #     ans.append(heapq.heappop(heap)[1]) # O(logn)
        #     k -= 1
        # return ans

        """
        time: O(n)
        space: O(n)
        approach: grouping into buckets
        """
        n = len(nums)
        bucket = [[] for _ in range(n+1)]
        counter = dict(Counter(nums))

        for ele in counter:
            bucket[counter[ele]].append(ele)

        ans = []
        i = n
        while k:
            eles = len(bucket[i])
            if 0 < eles <= k:
                ans.extend(bucket[i])
                k -= eles
            elif eles > k:
                ans.extend(bucket[i][:k])
                k = 0
            i -= 1
        return ans
            
        
        



        



        
        