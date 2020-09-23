class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def addPassenger(self, name):
        if not self.openSeats():
            return False
        self.passengers.append(name)
        return True

    def openSeats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Apoorv", "vApor", "7ummer", "winter"]

for person in people:
    success = flight.addPassenger(person)
    if success:
        print(f"Adding {person} to flight successfully")
    else:
        print(f"No available seat for {person}")