class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """o(nlog(n)) approach: sort and match"""

        s = sorted([ele for ele in s])
        t = sorted([ele for ele in t])

        return s == t
        