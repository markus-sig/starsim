'''
Created on 04.05.2018

@author: markus
'''
import random
from random import randint

class Ship():
    '''
    Main class for all ships
    '''


    def __init__(self):
        '''
        Constructor, will create a name and price
        '''
        self.name = str(randint(1000,9999))
        self.price = randint(1000,3000)
    
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
