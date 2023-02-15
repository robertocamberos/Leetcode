class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.count = 0
        self.size = size
        self.windowSum = 0
        

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        
        self.windowSum = self.windowSum - tail + val
        
        return self.windowSum / min(self.size, self.count)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)