class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = defaultdict(list)
        for ele in strs:
            count = [0]*26 #assuming lowercase english alphabets only
            for ch in ele:
                count[ord(ch) - ord('a')] += 1
            ans[tuple(count)].append(ele)
        
        return list(ans.values())
        
        