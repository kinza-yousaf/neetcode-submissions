class MyStack:
    # valid 
    # append, [0] for peek, popleft(), len

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        tmp = self.q[-1]
        del self.q[-1]
        return tmp

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not len(self.q)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()