class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check_valid(dic, base):
            for ch in base:
                if ch in dic and dic[ch] >= base[ch]:
                    pass
                else:
                    return False
            return True

        from collections import Counter, defaultdict
        i = j = 0
        n = len(s)
        base = Counter(t)
        mydic = defaultdict(int)
        ans = "0"*(n+1)
        while j < n:
            # expand until we get a valid substring
            mydic[s[j]] += 1

            # check if we found valid state
            while check_valid(mydic, base):
                if j - i + 1 <= len(ans):
                    ans = s[i:j+1]
                mydic[s[i]] -= 1
                i += 1

            j += 1
        return ans if not ans.count('0') else ""

            

        