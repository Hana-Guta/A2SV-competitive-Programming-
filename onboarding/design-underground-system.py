class UndergroundSystem:

    def __init__(self):
        self.journies = defaultdict(lambda : [0, 0])
        self.check_in = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, check_in_time = self.check_in[id]
        curr_journey = check_in_station + "->" + stationName

        self.journies[curr_journey][0] += t - check_in_time
        self.journies[curr_journey][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        target = startStation + "->" + endStation
        total_sum, amount = self.journies[target]

        return total_sum / amount
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)