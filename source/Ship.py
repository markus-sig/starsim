'''
Created on 04.05.2018

@author: markus
'''
import random
from random import randint

class Ship():
    '''
    Parent class for all ships
    '''
    def __init__(self):
        '''
        Constructor, will create a name and price
        '''
        self.name = str(randint(1000,9999))
        self.price = randint(1000,3000)
        self.maintenance = int(self.price*0.12)
    
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def getMaintenance(self):
        return self.maintenance
    
    def modifyPrice(self, planettype): #1 = agri, 2 = tech, 3 = war
        if (planettype == 1):
            self.price = self.price + 500
        elif (planettype == 2):
            self.price = self.price - 500
        else:
            self.price = self.price + 1500
            
    def toString(self):
        return ("Price: {}, Maintenance: {}".format(self.price, self.maintenance))
    
    
