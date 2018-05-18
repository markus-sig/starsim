'''
Created on 17.05.2018

@author: markus
'''
from CargoShip import CargoShip

class Player():
    
    def __init__(self, name):
     
        self.name = name
        self.credits = 5000
        self.fighterShips = []
        self.cargoShips = []
        self.freeCargoUnits = 0
        self.totalCargoUnits = 0
        self.totalFirePower = 0
        self.totalMaintenance = 0
        self.numberOfFighters = 0
        self.numberOfCargoShips = 0
        self.food = 0
        self.tech = 0
        
    def addFighterShip(self,ship):
        self.fighterShips.append(ship)
        self.numberOfFighters += 1
    def addCargoShip(self,ship):
        self.cargoShips.append(ship)
        self.numberOfCargoShips += 1
    
    def getFreeCargoSpace(self):
        return self.freeCargoUnits
    
    def updateCargoUnits(self):
        '''
        method to find out how much free cargo space is available
        '''
        self.totalCargoUnits = 0
        for s in self.cargoShips:
            self.totalCargoUnits += s.getCargoUnits()
                
        self.freeCargoUnits = self.totalCargoUnits - self.food - self.tech
        
    def updateFirePower(self):
        '''
        method to find out how much fire power is available
        '''
        self.totalFirePower = 0
        for s in self.fighterShips:
            self.totalFirePower += s.getFirepower()
        
    def getName(self):
        return self.name
    
    def printStats(self):
        print("Captain ",self.name)
        print("You have ",self.credits," credits")
        print("{} Fighters provide you with {} firepower".format(len(self.fighterShips), self.totalFirePower))
        print("{} Cargoships have {} food, {} tech and {} free units".format(len(self.cargoShips), self.food, self.tech, self.freeCargoUnits))
        print("Your total maintenance per planet jump = ",self.totalMaintenance)
    def getCredits(self):
        return self.credits 
    def setCredits(self, c):
        self.credits = c
        
    def getFood(self):
        return self.food
    def clearFood(self):
        self.food = 0
    def addFood(self, food):
        self.food += food
    def sellFood(self, food):
        self.food -= food
        
    def getTech(self):
        return self.tech
    def clearTech(self):
        self.tech = 0
    def addTech(self, tech):
        self.tech += tech
    def sellTech(self, tech):
        self.tech -= tech
        
        
    def updateMaintenance(self):
        self.totalMaintenance = 0
        for f in self.fighterShips:
            self.totalMaintenance += f.getMaintenance()
        for c in self.cargoShips:
            self.totalMaintenance += c.getMaintenance()
    def getTotalFirepower(self):
        return self.totalFirePower
    def getTotalMaintenance(self):
        return self.totalMaintenance
            