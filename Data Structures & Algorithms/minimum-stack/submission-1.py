class MinStack:

    # Stack |  Min
    # -3       -3
    # 0        -2
    # 1        -2
    # -2       -2

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_next = min(self.min_stack[-1], val) if self.min_stack else val
        self.min_stack.append(min_next)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
