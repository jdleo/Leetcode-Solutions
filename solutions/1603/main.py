class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # initiate array for car type capacities
        self.slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        # decrement slot for car type
        self.slots[carType] -= 1
        # return whether this slot has capacity left
        return self.slots[carType] >= 0