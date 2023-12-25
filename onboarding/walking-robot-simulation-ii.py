class Robot:

    def __init__(self, width: int, height: int):

        self.perimeter = 2*width + 2*(height - 2)
        self.pos = 0
        self.is_first = True

        self.bottom_r = width - 1
        self.top_r = self.bottom_r + (height - 1)
        self.top_l = self.top_r + (width - 1)

    def step(self, num: int) -> None:

        self.is_first = False
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:

        if 0 <= self.pos <= self.bottom_r:
            return [self.pos, 0]

        if self.bottom_r < self.pos <= self.top_r:
            return [self.bottom_r, self.pos - self.bottom_r]

        if self.top_r < self.pos <= self.top_l:
            return [self.bottom_r - (self.pos - self.top_r), self.top_r - self.bottom_r]
        
        return [0, self.top_r - self.bottom_r - (self.pos - self.top_l)]

    def getDir(self) -> str:
        
        if self.is_first or 0 < self.pos <= self.bottom_r:
            return 'East'

        if self.bottom_r < self.pos <= self.top_r:
            return 'North'

        if self.top_r < self.pos <= self.top_l:
            return 'West'
        
        return 'South'


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()