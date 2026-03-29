class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                freq = Counter(s[i:j+1])
                freq_list = list(freq.values())
                freq_list.sort(reverse=True)
                if sum(freq_list) - freq_list[0] <= k:
                    ans = max(ans, sum(freq_list))
        return ans

        


                

        