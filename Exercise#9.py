class Car():
    def __init__(self,r,s:int,c=0,d=0):
        self.registration = r
        self.maxspeed = s
        self.distance_travelled = int(d)
        self.current_speed = int(c)

    def accelerate(self,a:int):
        self.current_speed += a
        if self.current_speed > self.maxspeed:
            self.current_speed -= a
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self,h:float):
        self.distance_travelled = self.distance_travelled + self.current_speed*h

    def getDrive(self):
        return self.distance_travelled

    def printInfo(self):
        print(f"Registration Number: {self.registration}\n"
              f"Maximum Speed: {self.maxspeed}Km\h\n"
              f"Current Speed: {self.current_speed}Km\h\n"
              f"Distance Travelled: {self.distance_travelled}Km\n")



#Task 1
print("Task#1")
print()

Car1 = Car("NENC9CE",293)
Car2 = Car("KKEF32",180)
Car1.printInfo()
Car2.printInfo()


#Task 2
print("Task#2")
print()
Car1.accelerate(123)
Car1.accelerate(300)
Car1.printInfo()

Car2.accelerate(-123)
Car2.accelerate(150)
Car2.accelerate(-123)
Car2.printInfo()

#Task 3
print("Task#3")
print()

Car1.drive(2.423)
Car1.printInfo()
Car1.drive(1)
Car1.printInfo()
Car2.drive(0.5)
Car2.printInfo()
Car2.drive(2)
Car2.printInfo()

#Task 4
print("Task#4")
print()

import random
Racers = []
R = "ABC-"
c = 1

for i in range(1,11):
    Racers.append(Car(R+str(i),random.randint(100,200)))


TravelMax = 0
while TravelMax < 10_000:
    for i in Racers:
        i.accelerate(random.randint(-10,15))
        i.drive(1)
        TravelMax = max(i.distance_travelled,TravelMax)

for i in Racers:
    if i.distance_travelled >= 10_000:
        Winner = i.registration
    print(f"{i.registration}: {i.maxspeed}Km/h, Travelled: {i.distance_travelled}Km")
print()
print(f"The Winner is {Winner}!! He Drove {TravelMax}")