class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min, val) if self.min is not None else val
        

    def pop(self) -> None:
        if self.stack:
            if self.min == self.stack.pop():
                self.min = min(self.stack) if self.stack else None
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
