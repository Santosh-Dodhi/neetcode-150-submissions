class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """o(nlog(n)) approach: sort and match"""

        # return sorted(s) == sorted(t)

        """o(n) time and space"""
        # from collections import Counter

        # return Counter(s) == Counter(t)

        """o(n) time and space"""
        if len(s) != len(t):
            return False
        arr = [0]*26
        for ch in s:
            arr[ord(ch)-ord('a')] += 1

        for ch in t:
            arr[ord(ch)-ord('a')] -= 1
        
        for ele in arr:
            if ele != 0:
                return False
        return True
        

        