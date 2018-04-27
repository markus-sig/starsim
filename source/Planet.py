'''
Created on 27.04.2018

@author: markus
'''
import string
import random
class Planet(object):
    '''
    This class should represent a planet in the starsim game.
    There are three types of planets (int): agri (1), tech (2) and military (3)
    They all over the same type of goods, only prices will vary, so there
    seems no need for inheritance 
    '''


    def __init__(self, typeOfPlanet):
        '''
        Constructor will set the type of planet
        '''
        self.typeOfPlanet = typeOfPlanet
        self.name = self.createname()
        self.market = {"Food":1.0, "ConsumerGoods":1.0, "IndustrialGoods":1.0}
        self.shipyard
        
    def createname(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits, k=8))
        
        