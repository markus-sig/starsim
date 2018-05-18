'''
Created on 04.05.2018

@author: markus
'''
from Ship import Ship

class CargoShip(Ship):
    '''
    CargoClass, will inherite from Class Ship, plus it has storage space
    '''
    def __init__(self):
        '''
        Constructor, call super constructor and then add cargo space as % of price
        '''
        super().__init__()
        self.name = "C"+super().getName()
        self.cargoUnits = int(super().getPrice()*0.09725)
        
    
    def getCargoUnits(self):
        return self.cargoUnits
    
    def toString(self):
       return ("Name: {}, CargoUnits: {} ".format(self.name, self.cargoUnits)) + super().toString() 
    
        