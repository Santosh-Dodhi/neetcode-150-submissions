class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """o(nlog(n)) approach: sort and match"""

        return sorted(s) == sorted(t)

        """o(n) time and space"""
        # from collections import Counter

        # return Counter(s) == Counter(t)
        