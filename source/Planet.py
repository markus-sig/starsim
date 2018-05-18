'''
Created on 27.04.2018

@author: markus
'''
import string
import random
from FighterShip import FighterShip
from CargoShip import CargoShip
class Planet():
    '''
    This class should represent a planet in the starsim game.
    There are three types of planets (int): agri (1), tech (2) and war (3)
    They all over the same type of goods, only prices will vary, so there
    is no need for inheritance 
    '''

    def __init__(self, typeOfPlanet):
        '''
        Constructor will set the type of planet
        '''
        self.typeOfPlanet = typeOfPlanet
        self.name = self.createname()
        self.market = self.market()
        self.shipyard = self.shipyard()
        
    def createname(self):
        info = ""
        if (self.typeOfPlanet == 1):
            info = " - AgroPlanet "
        elif (self.typeOfPlanet == 2):
            info = " - TechPlanet "
        else:
            info = " - This planet is torn asunder by war"
        name = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        return name + info
        
    def shipyard(self):
        '''
        methode um zufaellig eine Liste mit Schiffen anzulegen
        '''
        shipList = []
        if (self.typeOfPlanet == 1):  #agri
            upperLimit = 3
        elif (self.typeOfPlanet == 2):  #tech
            upperLimit = 4
        else: #war
            upperLimit = 1
     
        for i in range(0,random.randint(1,upperLimit)):
            fs = FighterShip()
            fs.modifyPrice(self.typeOfPlanet)
            shipList.append(fs)
        for i in range(0,random.randint(1,upperLimit)):
            cs = CargoShip()
            cs.modifyPrice(self.typeOfPlanet)
            shipList.append(cs)
        return shipList
    
    def market(self):
        if (self.typeOfPlanet == 1):  #agri
            marketPlace = {"Food":random.randint(10,20), "Tech":random.randint(30,50)}
        elif (self.typeOfPlanet == 2):  #tech
            marketPlace = {"Food":random.randint(20,40), "Tech":random.randint(20,40)}
        else: #war
            marketPlace = {"Food":random.randint(40,60), "Tech":random.randint(50,70)}
        
        return marketPlace
    
    def getMarket(self):
        return self.market
    def getShipyard(self):
        return self.shipyard
    def getName(self):
        return self.name
    
        
        