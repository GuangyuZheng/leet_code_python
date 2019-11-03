class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_record = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.min_record) == 0 or x < self.min_record[-1]:
            self.min_record.append(x)
        else:
            self.min_record.append(self.min_record[-1])

    def pop(self) -> None:
        self.data = self.data[:-1]
        self.min_record = self.min_record[:-1]

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_record[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
