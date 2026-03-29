class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return "ππ"
        if strs == [""]: return "πππ"
        return 'π'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "ππ": return []
        if s == "πππ": return [""]
        return s.split('π')
