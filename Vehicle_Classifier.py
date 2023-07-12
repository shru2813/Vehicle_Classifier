class Vehicle:
    def Start(self):
        print("Vehicle Started")
    def Stop(self):
        print("Vehicle Stopped")
class Car(Vehicle):
     def Start(self):
         print("Car Started")
     def Stop(self):
         print("Car Stopped")
class MotorCycle(Vehicle):
    def Start(self):
        print("MotorCycle Started")
    def Stop(self):
        print("MotorCycle Stopped")
if __name__ == '__main__':
    obj1=Vehicle()
    obj1.Start()
    obj1.Stop()
    print() #for space
    obj2=Car()
    obj2.Start()
    obj2.Stop()
    print()#for space
    obj3=MotorCycle()
    obj3.Start()
    obj3.Stop()
