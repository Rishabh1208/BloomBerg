# creating your class to make it more extensible.

# Time complexity would be o(1) for every operation.
# space complexity would be O(n+m)
# n - hashmap of arrival time and m - hashmap of average time.

# Follow ups - what if station name could have spaces before and after (we could use strip())
# id, station name, time
class Event:
    def __init__(self, id, stationName, time):
        self.id = id
        self. stationName = stationName
        self.time = time

# get average
class Average:
    def __init__(self):
        self.count = 0
        self.total = 0

    def updateAverage(self, diff):
        self.count += 1
        self.total += diff

    def getAverage(self):
        return self.total / self.count

# Design an UnderGround system
class UndergroundSystem(object):

    def __init__(self):
        self.arrivals = {}
        self.averages = {}

    def checkIn(self, id, stationName, t):
        self.arrivals[id] = Event(id, stationName, t)

    def checkOut(self, id, stationName, t):
        arrivalEvent = self.arrivals.pop(id)
        diff = t - arrivalEvent.time
        key = (arrivalEvent.stationName, stationName)
        average = self.averages.get(key, Average())
        average.updateAverage(diff)
        self.averages[key] = average

    def getAverageTime(self, startStation, endStation):
        key = (startStation, endStation)
        return self.averages[key].getAverage()


undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
undergroundSystem.checkOut(27, "Waterloo", 20)
undergroundSystem.checkOut(32, "Cambridge", 22)
undergroundSystem.getAverageTime("Paradise", "Cambridge")
undergroundSystem.getAverageTime("Leyton", "Waterloo")
undergroundSystem.checkIn(10, "Leyton", 24)
undergroundSystem.getAverageTime("Leyton", "Waterloo")
undergroundSystem.checkOut(10, "Waterloo", 38)
undergroundSystem.getAverageTime("Leyton", "Waterloo")
