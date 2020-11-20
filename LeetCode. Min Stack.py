class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, x):
        if len(self.stack) == 0 or len(self.minimum) == 0:
            self.minimum.append([x, 1])
        else:
            if x < self.getMin():
                self.minimum.append([x, 1])
            elif x == self.getMin():
                self.minimum[-1][1] += 1
        self.stack.append(x)

    def pop(self):
        if self.stack[-1] == self.minimum[-1][0]:
            self.stack.pop(-1)
            if (self.minimum[-1][1] > 1):
                self.minimum[-1][1] -= 1
            else:
                self.minimum.pop(-1)
        else:
            self.stack.pop(-1)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minimum[-1][0]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(200)
obj.push(5)
obj.push(35)
obj.push(-9)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())