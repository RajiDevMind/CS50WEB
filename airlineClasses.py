# object oriented  programming fudamentals with class

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def  addPassenger(self, name):
        if not self.availableSeats():
            return False
        self.passengers.append(name)
        return True
    def availableSeats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

travellers = ["sanwoolu", "tinubu", "makinde", "davido"]
for person in travellers:
    success = flight.addPassenger(person)
    if success:
        print(f"Successfully add {person}")
    else:
        print(f"No  available seat for {person}")
