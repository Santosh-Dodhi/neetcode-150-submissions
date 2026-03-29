class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = j = 0
        max_len = 0
        window = set()
        while j < n:
            while j < n and s[j] not in window:
                window.add(s[j])
                j += 1
            
            max_len = max(max_len, len(window))

            while i <= j and j < n and s[j] in window:
                window.remove(s[i])
                i += 1
        return max_len
        