'''
Name: Amna (23k-0066)
Assignment#1 of PAI
'''

class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
        self.is_available = True

    def mark_availability(self, available):
        self.is_available = available

    def display_info(self):
        info = f"Name: {self.name}\nAge: {self.age}\nHabitat: {self.habitat}\nAvailability Status: {'viewing' if self.is_available else 'quarantine'}"
        return info


class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_length, diet_type):
        super().__init__(name, age, habitat)
        self.fur_length = fur_length
        self.diet_type = diet_type

    def display_info(self):
        base_info = super().display_info()
        unique_info = f"\nFur Length: {self.fur_length}\nDiet Type: {self.diet_type}"
        return base_info + unique_info


class Bird(Animal):
    def __init__(self, name, age, habitat, wingspan, flight_altitude):
        super().__init__(name, age, habitat)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude

    def display_info(self):
        base_info = super().display_info()
        unique_info = f"\nWingspan: {self.wingspan}\nFlight Altitude: {self.flight_altitude}"
        return base_info + unique_info


class Reptile(Animal):
    def __init__(self, name, age, habitat, scale_pattern, venomous_status):
        super().__init__(name, age, habitat)
        self.scale_pattern = scale_pattern
        self.venomous_status = venomous_status

    def display_info(self):
        base_info = super().display_info()
        unique_info = f"\nScale Pattern: {self.scale_pattern}\nVenomous: {self.venomous_status}"
        return base_info + unique_info


info = lambda *animals: [print(animal.display_info(), "\n") for animal in animals]

if __name__ == "__main__":
    mammal = Mammal("Elephant", 10, "Savannah", "Short", "Herbivore")
    bird = Bird("Eagle", 5, "Mountains", "2.5m", "3000m")
    reptile = Reptile("Python", 3, "Rainforest", "Striped", "Non-venomous")

    info(mammal, reptile, bird)

    mammal.mark_availability(False)
    reptile.mark_availability(False)

    print("\nAfter changing availability status:")
    info(mammal, reptile, bird)
