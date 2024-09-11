'''
Programmer: Amna(23k-0066)
Date: 11/Sept/2024
Q7) Create a Bus child class that inherits from the Vehicle class. The default fare charge of any
    vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10%
    on full fare as a maintenance charge. So total fare for bus instance will become the final
    amount = total fare + 10% of the total fare.
'''

class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def calculate_fare(self):
        return self.seating_capacity * 100

class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def calculate_fare(self):
        base_fare = super().calculate_fare()
        maintenance_charge = 0.10 * base_fare
        total_fare = base_fare + maintenance_charge
        return total_fare

# Example usage
if __name__ == "__main__":
    bus = Bus(seating_capacity=40)
    fare = bus.calculate_fare()
    print(f"Total fare for the bus: ${fare:.2f}")
