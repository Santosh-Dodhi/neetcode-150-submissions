class MinStack:
    """
    time: O(1)
    space: O(2n) where n is the len(stack)
    approach: 2 stacks
    """
    # def __init__(self):
    #     self.stack = []
    #     self.minStack = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.minStack:
    #         self.minStack.append(val)
    #     elif val < self.minStack[-1]:
    #         self.minStack.append(val)
    #     else:
    #         self.minStack.append(self.minStack[-1])

    # def pop(self) -> None:
    #     if self.stack:
    #         self.stack.pop()
    #         self.minStack.pop()
        
    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.minStack[-1]

    """
    time: O(1)
    space: O(n) for stack only
    approach: 1 stack
    """
    def __init__(self):
        self.stack = []
        self.min_ele = None
    
    def push(self, val:int) -> None:
        if not self.stack:
            self.min_ele = val
        encoded = val - self.min_ele
        self.stack.append(encoded)
        if encoded < 0:
            self.min_ele = val
    
    def pop(self) -> None:
        encoded = self.stack.pop()
        if encoded < 0:
            self.min_ele = self.min_ele - encoded
    
    def top(self) -> int:
        encoded = self.stack[-1]
        if encoded < 0:
            return self.min_ele
        return encoded + self.min_ele
    
    def getMin(self) -> int:
        return self.min_ele




        
