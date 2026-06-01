class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        self.smallest = float('inf')        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min:
            current_min = min(val, self.min[-1])
        else:
            current_min = val
        self.min.append(current_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
