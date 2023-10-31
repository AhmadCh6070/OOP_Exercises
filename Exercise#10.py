# class Building():
#     def __init__(self,t:int,b:int,n:int):
#         self.bottom = b
#         self.property = []
#         for i in range (n):
#             self.property.append(Elevator(b,t))
#
#     def run_elevator(self,n:int,f:int):
#         if n <= len(self.property):
#             selected_Lift = self.property[0:n]
#             for i in selected_Lift:
#                 i.go_to_floor(f)
#         else:
#             print("Incorrect Number of Floors Entered")
#             print()
#
#     def fire_alarm(self):
#         print("The Fire Alarm Has Been Activated! Returning All Elevators to the Bottom Floor!")
#         print()
#         for i in self.property:
#             i.go_to_floor(self.bottom)
#
#     def printFloor(self):
#         for i in self.property:
#             i.printInfo()
#
#
#
# class Elevator():
#     def __init__(self,b:int,t:int):
#         self.bottom = b
#         self.current_floor = self.bottom
#         self.top= t
#
#     def floor_up(self):
#         if (self.current_floor + 1) <= self.top:
#             print("Moved One Floor Up")
#             print()
#             self.current_floor += 1
#         else:
#             print("Cannot go above the Top Floor")
#             print()
#
#     def floor_down(self):
#         if (self.current_floor - 1) >= self.bottom:
#             print("Moved One Floor Down")
#             print()
#             self.current_floor += 1
#         else:
#             print("Cannot go below the Top Floor")
#             print()
#
#     def go_to_floor(self,f:int):
#         if f >= self.bottom and f <= self.top:
#             self.current_floor = f
#
#
#     def printInfo(self):
#         print(f"Current Floor: {self.current_floor}\n"
#               f"Top Floor: {self.top}\n"
#               f"Bottom Floor: {self.bottom}")
#         print()
#
# #Task 1
# print("Task#1")
# print()
# Lift =Elevator(0,6)
# Lift.floor_up()
# Lift.floor_up()
# Lift.floor_down()
# Lift.go_to_floor(6)
# Lift.go_to_floor(-2)
# Lift.printInfo()
#
# #Task 2
# print("Task#2")
# print()
# Building = Building(6,0,7)
# Building.run_elevator(5,9)
# Building.printFloor()
# Building.run_elevator(6,2)
# Building.printFloor()
#
# #Task 3
# print("Task#3")
# print()
# Building.fire_alarm()
# Building.printFloor()
#
#Task 4
import random

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

    def hour_passes(self):
        self.drive(1)
        self.race_finished()


    def race_finished(self):
        if self.distance_travelled > 500:
            return True

    def drive(self,h:float):
        self.distance_travelled = self.distance_travelled + self.current_speed*h

    def getDrive(self):
        return self.distance_travelled

    def printStatus(self):
        print(f"Registration Number: {self.registration}\n"
              f"Distance Travelled: {self.distance_travelled}Km\n")

Grand_Demolition_Derby = []
R = "ABC-"
c = 1

for i in range(1,11):
    Grand_Demolition_Derby.append(Car(R+str(i),random.randint(100,200)))

hour = 1

while True:
    for racer in Grand_Demolition_Derby:
        racer.accelerate(random.randint(-10,15))
        racer.hour_passes()
        if racer.race_finished():
            break
    print(hour)
    hour += 1
    if hour%10 == 0:
        for details in Grand_Demolition_Derby:
            details.printStatus()
    if racer.race_finished():
        Winner = racer
        for details in Grand_Demolition_Derby:
            details.printStatus()
        break
print(f"Winner is {Winner.registration}!! He travelled {Winner.distance_travelled}Km in just {hour} Hours!")



