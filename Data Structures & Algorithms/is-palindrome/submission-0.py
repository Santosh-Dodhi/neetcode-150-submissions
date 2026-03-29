class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        allowed = set('abcdefghijklmnopqrstuvwxyz')
        allowed.update(set('0123456789'))
        new_s = ""
        for ch in s:
            if ch not in allowed:
                continue
            else:
                new_s += ch
        print(new_s)
        return new_s == new_s[::-1]

        