#Task 1
class Author:
    def __init__(self,name):
        self.name = name
    def print_information(self):
        print(f"Author Name: {self.name}")

class Book(Author):
    def __init__(self,book_name,author_name,pages:int):
        super().__init__(author_name)
        self.book = book_name
        self.pages = pages

    def print_information(self):
        print(f"Book Name: {self.book}") 
        super().print_information()
        print(f"Pages: {self.pages}")
        print()


class Magazine(Author):
    def __init__(self,mag_name,chief):
        super().__init__(chief)
        self.mag = mag_name

    def print_information(self):        
        print(f"Magazine Name: {self.mag}") 
        super().print_information()
        print()

#Task 1
print("Task#1")

Book1 = Book("Harry Potter","ALi",2123)
Mag1 = Magazine("How to do Java","Ahmad")
Book2 = Book("Compartment No.6","Rosa Liksom", 192)
Mag2 = Magazine("Donald Duck","Aki Hyyppä")
Book1.print_information()
Book2.print_information()
Mag1.print_information()
Mag2.print_information()

#Task 2
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.kilometers_driven = 0

    def drive(self, hours, speed):
        distance = hours * speed
        self.kilometers_driven += distance


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


# Creating instances of ElectricCar and GasolineCar
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

# Selecting speeds for both cars and driving for three hours
electric_speed = 120  # km/h
gasoline_speed = 180  # km/h

electric_car.drive(3, electric_speed)
gasoline_car.drive(3, gasoline_speed)

# Printing out the values of their kilometer counters
print(f"Electric car kilometers driven: {electric_car.kilometers_driven} km")
print(f"Gasoline car kilometers driven: {gasoline_car.kilometers_driven} km")


