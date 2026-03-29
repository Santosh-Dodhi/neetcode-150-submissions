class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        time: o(n)
        space: o(n)
        """
        # s = s.lower()
        # allowed = set('abcdefghijklmnopqrstuvwxyz')
        # allowed.update(set('0123456789'))
        # new_s = ""
        # for ch in s:
        #     if ch not in allowed:
        #         continue
        #     else:
        #         new_s += ch
        # print(new_s)
        # return new_s == new_s[::-1]

        n = len(s)
        i = 0
        j = n-1
        allowed = set("abcdefghijklmnopqrstuvwxyz")
        allowed.update(set("0123456789"))
        s = s.lower()
        while i <= j:
            while i<=j and s[i] not in allowed:
                i += 1
            while i<=j and s[j] not in allowed:
                j -= 1
            if i <= j and s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

                
        