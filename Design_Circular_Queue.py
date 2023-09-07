class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.k = k
        
    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue = [value] + self.queue
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value) #push in last
            return True
        return False
        
    def deleteFront(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if len(self.queue) > 0:
            self.queue.pop()
            return True
        return False

    def getFront(self) -> int:
        if len(self.queue) > 0:
            front = self.queue[0]
            return front
        return -1

    def getRear(self) -> int:
        if len(self.queue) > 0:
            last = self.queue[-1]
            return last
        return -1
        
    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if len(self.queue) == self.k:
            return True
        return False
        
