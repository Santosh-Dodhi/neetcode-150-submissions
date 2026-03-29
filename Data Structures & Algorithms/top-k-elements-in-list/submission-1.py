class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """o(n) time + o(n) space complexity"""
        from collections import Counter

        counter = Counter(nums)
        ans = list()
        sorted_items = sorted(counter.items(), key= lambda x: x[1], reverse=True)
        # print(sorted_items)

        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans

        