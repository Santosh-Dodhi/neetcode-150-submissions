class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ele_st = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_ele_st:
            self.min_ele_st.append(val)
        elif val < self.min_ele_st[-1]:
            self.min_ele_st.append(val)
        else:
            self.min_ele_st.append(self.min_ele_st[-1])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_ele_st.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_ele_st[-1]
        
