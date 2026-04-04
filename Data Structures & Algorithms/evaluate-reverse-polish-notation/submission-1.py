class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        j = 0
        n = len(tokens)
        while j < n:
            if tokens[j] not in operators:
                stack.append(int(tokens[j]))
            else:
                b = stack.pop()
                a = stack.pop()
                if tokens[j] == "+":
                    stack.append(a+b)
                elif tokens[j] == "-":
                    stack.append(a-b)
                elif tokens[j] == "*":
                    stack.append(a*b)
                elif tokens[j] == "/":
                    stack.append(int(a/b)) # // not work
            print(j, stack)
            j += 1
        return stack[-1]

        


        