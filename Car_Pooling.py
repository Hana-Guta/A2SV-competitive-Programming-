class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = []
        for count, start, end in trips:
            arr.append((start, count))
            arr.append((end, -count))
        arr.sort()

        inCar = 0
        for destination, passangers in arr:
            inCar += passangers
            if inCar > capacity:
                return False
        return True
