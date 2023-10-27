class Building():
    def __init__(self):

class Elevator():
    def __init__(self,b:int,t:int):
        self.bottom = b
        self.current_floor = self.bottom
        self.top= t

    def floor_up(self):
        if (self.current_floor + 1) <= self.top:
            print("Moved One Floor Up")
            print()
            self.current_floor += 1
        else:
            print("Cannot go above the Top Floor")
            print()

    def floor_down(self):
        if (self.current_floor - 1) >= self.bottom:
            print("Moved One Floor Down")
            print()
            self.current_floor += 1
        else:
            print("Cannot go below the Top Floor")
            print()

    def go_to_floor(self,f:int):
        if f >= self.bottom and f <= self.top:
            self.current_floor = f
            print(f"Elevator has arrived at {self.current_floor}")
            print()
        else:
            print("Floor Doesn't Exist")
            print()

    def printInfo(self):
        print(f"Current Floor: {self.current_floor}\n"
              f"Top Floor: {self.top}\n"
              f"Bottom Floor: {self.bottom}")
        print()

#Task 1
print("Task#1")
print()
Lift =Elevator(0,6)
Lift.floor_up()
Lift.floor_up()
Lift.floor_down()
Lift.go_to_floor(6)
Lift.go_to_floor(-2)
Lift.printInfo()

#Task 2
print("Task#2")
print()

