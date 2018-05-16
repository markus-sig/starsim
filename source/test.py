'''
Created on 14.05.2018

@author: markus
'''


from Ship import Ship
from CargoShip import CargoShip
from FighterShip import FighterShip



s = Ship()
s2 = CargoShip()
s3 = FighterShip()
print("name=",s.getName())
print("name=",s2.getName())
print("price=",s2.getPrice())
print("cargounits=",s2.getCargoUnits())
print("firepower=",s3.getFirepower())
