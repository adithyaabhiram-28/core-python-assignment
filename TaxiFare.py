class Taxi:
    base = 50
    distFare = 10
    def __init__(self,trips):
        self.trips = trips
    def totalFare(self):
        self.total = []
        for trip in self.trips:
            self.total.append(self.base + (self.distFare * trip))
        return self.total
    
    
trips = [5, 10, 3]

taxi = Taxi(trips)
total = taxi.totalFare()
tot = 0
for i in range(len(total)):
    print(f"Trip {i+1}: ${total[i]}")
    tot += total[i]
print(f"Total Fare for all trips: ${tot}")