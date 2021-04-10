import random

#Vehicle Class
class Vehicle:
    def __init__(self, Make="Make",Model="Model",Year=0,Weight=0):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0
        

    def setMake(self, Make):
            self.Make = Make

    def setModel(self, Model):
            self.Model = model

    def setYear(self, Year):
            self.Year = Year

    def setWeight(self, Weight):
            self.Weight = Weight

    def getMaintenanceStatus(self):
        return self.NeedsMaintenance

    def getTripsSinceMaintenance(self):
        return self.TripsSinceMaintenance

    def Repair(self):
        if self.NeedsMaintenance:
            self.TripsSinceMaintenance = 0
            self.NeedsMaintenance = False

#Cars Class
class Cars(Vehicle):
    def __init__(self, Make="Make",Model="Model",Year=0,Weight=0):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.isDriving = False


    def Drive(self):
        if not self.isDriving:
            self.isDriving = True
            return True
        else:
            return False

    def Stop(self):
        if self.isDriving:
            self.isDriving = False
            self.TripsSinceMaintenance+= 1
            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = True
            return True
        else:
            return False

    def __str__(self):
        return "The car is " + self.Make + " " + self.Model + " from year " + str(self.Year) + " and weighs " + str(
            self.Weight) + "\nCurrently has been driven " + str(
            self.TripsSinceMaintenance) + " times and " + (
                   "needs " if self.NeedsMaintenance else " doesn't need ") + "maintenance.\n"

#Plane Class

class Planes(Vehicle):
    def __init__(self, Make, Model, Year, Weight):
        Vehicle.__init__(self, Make, Model, Year, Weight)
        self.isFlying = False

    def Fly(self):
        if not self.getMaintenanceStatus():
            if not self.isFlying:
                self.isFlying = True
                return True
            else:
                return False
        else:
            print("Plane needs to be repaired before flying again.")

    def Land(self):
        if self.isFlying:
            self.isFlying = False
            self.TripsSinceMaintenance+= 1
            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = True
            return True
        else:
            return False

    def __str__(self):
        return "The plane is " + self.Make + " " + self.Model + " from year " + str(self.Year) + " and weights " + str(
            self.Weight) + "\nCurrently has been driven " + str(
            self.TripsSinceMaintenance) + " times and " + (
                   "needs " if self.NeedsMaintenance else " doesn't need ") + "maintenance.\n"

   
#Main

Maruti = Cars("MarutiSuzuki", "Ertiga", 2017, 1235)
Tiago = Cars("Tata", "Tiago", 2015, 991)
EcoSport = Cars("Ford", "Ecosport", 2019, 1309)
Boeing = Planes("Boeing","555-500LR",2018,223168)


for i in range(random.randrange(300)):
    Maruti.Drive()
    Maruti.Stop()

for i in range(random.randrange(300)):
    Tiago.Drive()
    Tiago.Stop()

for i in range(random.randrange(300)):
    EcoSport.Drive()
    EcoSport.Stop()

for i in range(random.randrange(300)):
    Boeing.Fly()
    Boeing.Land()

print(Maruti)
print(Tiago)
print(EcoSport)
print(Boeing)
    

    

    
        
        
            
            
        
