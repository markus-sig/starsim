'''
Created on 04.05.2018

@author: markus
'''
from Ship import Ship

class FighterShip(Ship):
    '''
    FighterClass, will inherite from Class Ship, plus it has fire power
    '''


    def __init__(self):
        '''
        Constructor, call super constructor and then add firepower as % of price
        '''
        super().__init__()
        self.name = "F"+super().getName()
        self.firepower = int(super().getPrice()*0.09725)
        
    
    def getFirepower(self):
        return self.firepower
    
        