class Solution:
    """using non ascii character π as the separator"""
    # def encode(self, strs: List[str]) -> str:
    #     if strs == []: return "ππ"
    #     if strs == [""]: return "πππ"
    #     return 'π'.join(strs)

    # def decode(self, s: str) -> List[str]:
    #     if s == "ππ": return []
    #     if s == "πππ": return [""]
    #     return s.split('π')

    def encode(self, strs: List[str]) -> str:
        s = ""
        for ele in strs:
            s += str(len(ele)) + ','
        
        s += '#'
        for ele in strs:
            s += ele
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        if s=="#": return []
        lens, strs = s.split(',#', 1)
        num_lens = lens.split(',')
        print(num_lens)
        num_lens = [int(ele) for ele in num_lens]
        ans = []
        st = 0
        for ele in num_lens: 
            string = strs[st:st+ele]
            ans.append(string)
            st = st+ele
        return ans
            
