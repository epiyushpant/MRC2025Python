class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")

class LandVehicle(Vehicle):
    def __init__(self, brand, wheels):
        super().__init__(brand)
        self.wheels = wheels

    def show_wheels(self):
        print(f"Wheels: {self.wheels}")

class WaterVehicle(Vehicle):
    def __init__(self, brand, max_depth):
        super().__init__(brand)
        self.max_depth = max_depth

    def show_max_depth(self):
        print(f"Max Depth: {self.max_depth} meters")

class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, brand, wheels, max_depth):
        LandVehicle.__init__(self, brand, wheels)
        WaterVehicle.__init__(self, brand, max_depth)

    def show_info(self):
        self.show_brand()
        self.show_wheels()
        self.show_max_depth()

# Usage
amphibious = AmphibiousVehicle("AmphiCorp", 4, 20)
amphibious.show_info()
