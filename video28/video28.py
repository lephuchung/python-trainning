class Car:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"You are driving a {self.color} {self.brand} {self.name} ")

vios = Car("Vios", 'Toyota', 'blue')
vios.drive()
maybach = Car("Maybach", 'Mercedes', 'black')
maybach.drive()