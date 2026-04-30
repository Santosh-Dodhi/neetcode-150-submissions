class Solution:
    def isValid(self, s: str) -> bool:
        """
        time: O(n)
        space: O(n)
        approach: stack
        """
        # stack = []
        # mapping = {"(": ")", "{": "}", "[": "]"}
        # for ele in s:
        #     if ele in {'(', '{', '['}:
        #         stack.append(ele)
        #     elif stack and mapping[stack[-1]] == ele:
        #         stack.pop()
        #     else:
        #         return False
        # return True if not stack else False


        """
        time:
        space:
        approach:
        """
        # while '{}' in s or '()' in s or '[]' in s:
        #     s = s.replace('{}', '')
        #     s = s.replace('()', '')
        #     s = s.replace('[]', '')
        
        # if s == "": 
        #     return True
        # else: 
        #     return False













        opening = set({'(', '{', '['})
        n = len(s)
        i = 0
        stack = []
        dic = {
            '(': ')', '[': ']', '{': '}'
        }
        while i < n:
            if s[i] in opening:
                stack.append(s[i])
            elif stack and dic[stack[-1]] == s[i]:
                stack.pop()
            else:
                return False
            i += 1
        return True if not stack else False

                
        