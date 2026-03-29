class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """o(nlogn) time + o(n) space complexity"""
        # from collections import Counter

        # counter = Counter(nums)
        # ans = list()
        # sorted_items = sorted(counter.items(), key= lambda x: x[1], reverse=True)
        # # print(sorted_items)

        # for i in range(k):
        #     ans.append(sorted_items[i][0])

        # return ans

        """count frequency o(n) + heap o(nlogk)"""
        # from collections import Counter
        # import heapq
        # counter = Counter(nums)

        # heap = []
        # ans = []
        # for ele, freq in counter.items():
        #     heapq.heappush(heap, (freq, ele))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # while heap:
        #     ans.append(heapq.heappop(heap)[1])
        # return ans

        """count frequency o(n) + freq. bucket o(n)"""

        from collections import Counter
        counter = Counter(nums)
        n = len(nums)
        freq_arr = [[] for _ in range(n+1)]
        for ele, freq in counter.items():
            freq_arr[freq].append(ele)
        
        ans = []
        count = 0
        for bucket in freq_arr[::-1]:
            for ele in bucket:
                ans.append(ele)
                count += 1
                
                if count == k:
                    return ans
        


        

        