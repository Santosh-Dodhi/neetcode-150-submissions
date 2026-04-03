class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        counter = list(Counter(nums).items())
        heap = [(-y, x) for x,y in counter]

        heapq.heapify(heap)

        ans = []
        while k:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans

        



        
        