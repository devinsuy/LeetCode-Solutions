from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        # Map (src, dst) tuple to a running sum of trip length,
        # Map tuple to the amount of trips taken on this rought
        self.tripLenSum = defaultdict(int)
        self.tripCount = defaultdict(int)
        
        # Map passenger ID to (src, departTime) tuple of enroute trip
        self.idTrip = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idTrip[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Update the amount of trips between src, dst along with its trip length sum
        srcStation, tInit = self.idTrip[id]
        trip = (srcStation, stationName)
        self.tripCount[trip] += 1
        self.tripLenSum[trip] += (t - tInit)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = (startStation, endStation)
        return self.tripLenSum[trip] / self.tripCount[trip]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)