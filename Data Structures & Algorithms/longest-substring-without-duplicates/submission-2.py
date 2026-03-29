class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        time: O(2n) => O(n)
        space: O(n)
        approach: window set
        """
        # n = len(s)
        # i = j = 0
        # max_len = 0
        # window = set()
        # while j < n:
        #     while j < n and s[j] not in window:
        #         window.add(s[j])
        #         j += 1
            
        #     max_len = max(max_len, len(window))

        #     while i <= j and j < n and s[j] in window:
        #         window.remove(s[i])
        #         i += 1
        # return max_len

        """
        time: O(n) => O(n)
        space: O(n)
        approach: window dict 
        """
        n = len(s)
        i = j = 0
        max_len = 0
        dic = dict()
        while i <= j < n:
            while (j < n and s[j] not in dic) or (j< n and dic[s[j]] < i):
                dic[s[j]] = j
                j += 1
            max_len = max(max_len, j-i)
            if j < n:
                # i = dic.pop(s[j]) + 1 # returns index
                i = dic[s[j]] + 1
        return max_len
            
            



        