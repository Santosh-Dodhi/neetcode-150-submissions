class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")", "{": "}", "[": "]"}
        for ele in s:
            if ele in {'(', '{', '['}:
                stack.append(ele)
            elif stack and mapping[stack[-1]] == ele:
                stack.pop()
            else:
                return False
        return True if not stack else False

                
        