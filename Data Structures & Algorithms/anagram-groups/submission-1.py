class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """o(N*(n*log(n)) + NlogN + N)"""
        """Following algo(lexi-sorting each ele) will not work 
        as we need to return the exact ele """
        # strs = [sorted(ele) for ele in strs]

        # strs = sorted(strs)

        # ans = []
        # n = len(strs)
        # i = 0
        # while i < n-1:
        #     count = 1
        #     while i < n-1 and strs[i] == strs[i+1]:
        #         i += 1
        #         count += 1
        #     ans.append([strs[i]]*count)
        #     i += 1
        # return ans

        """O(N*n)+ O(N):frequency approach"""
        from collections import Counter, defaultdict
        counters = [Counter(ele).items() for ele in strs]
        # print(counters)
        ans = defaultdict(list)
        for i, ele in enumerate(counters):
            key = tuple(sorted(ele))
            ans[key].append(strs[i])

        # print(ans)
        return list(ans.values())
                

                


        