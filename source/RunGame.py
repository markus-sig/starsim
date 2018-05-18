'''
Created on 17.05.2018

@author: markus
'''
import Ship
import Player
import Planet
import random
from FighterShip import FighterShip

turnCounter = 0

def cleanScreen():
    for i in range(0,50):
        print("")
        
def spacePirates(player):#space prites attack, their firepower is +/-20% of player firepower
    while True:# loop
        cleanScreen()
        print("*****F*U*C*K****S*P*A*C*E*P*I*R*A*T*E*S***A*T*T*A*C*K*****")
        playerFirepower = player.getTotalFirepower()
        piratesFirepower = int(playerFirepower*(1+random.randint(-20,20)/100))
        if ((random.randint(0,playerFirepower) > playerFirepower/3) and 
            (random.randint(0,piratesFirepower) < piratesFirepower/3) or (playerFirepower == 0)):
            print("Damm, you got robbed by the pirates!")
            print("You lost all your cargo and half your money!")
            player.clearTech()
            player.clearFood()
            player.updateCargoUnits()
            player.setCredits(player.getCredits()/2)
        else:
            print("Lucky you! Your fighters drove them off!")
        print("**********************************************************")
        input("Hit enter to continue")
        break
        

def shipyardMenu(player, planet):
    while True:# loop
        cleanScreen()
        print("*****W*E*L*C*O*M*E****T*O****T*H*E****S*H*I*P*Y*A*R*D*****")
        player.printStats()
        print("**********************************************************")
        shipList = planet.getShipyard()
        print("Available Ships:")
        print("**********************************************************")
        i = 0
        for s in shipList:
            print("Nr.:"+str(i)+":"+s.toString())
            i += 1
        print("**********************************************************")  
        userInput = input("Enter the number you would like to by or x to leave:") 
        if (userInput == "x"):
            break;
        else:
            ui = int(userInput)
            if (ui <= i):
                if(player.getCredits() > shipList[ui].getPrice()): #has enough money
                    if(type(shipList[ui]) == FighterShip):
                        player.addFighterShip(shipList[ui])
                        player.updateFirePower()
                    else:
                        player.addCargoShip(shipList[ui])
                        player.updateCargoUnits()
                    player.setCredits(player.getCredits() - shipList[ui].getPrice())
                    player.updateMaintenance()
                    del shipList[ui]
            else:
                print("wrong number, try again ....")

def spacePortMenu(player, planet):
    global turnCounter
    while True:# loop
        cleanScreen()
        print("****W*E*L*C*O*M*E****T*O****T*H*E****S*P*A*C*E*P*O*R*T****")
        print("Enter 1 to jump to a agri planet (risk  5%)")
        print("Enter 2 to jump to a tech planet (risk 10%)")
        print("Enter 3 to jump to a war planet  (risk 20%)")
        userInput = input("Or enter x to exit:")
        risk = 0
        if (userInput == "x"):
            return planet
        elif (userInput == "1"):
            risk = 5
        elif(userInput == "2"):
            risk = 10
        else:
            risk = 20     
        if (random.randint(0,100) <= risk):
            spacePirates(player)
        player.setCredits(player.getCredits() - player.getTotalMaintenance())
        turnCounter += 1  
        return Planet.Planet(int(userInput))
            
def marketMenu(player, planet):
    while True:# loop
        cleanScreen()
        print("*******W*E*L*C*O*M*E****T*O****T*H*E****M*A*R*K*E*T*******")
        player.printStats()
        print("**********************************************************")
        market = planet.getMarket()
        print("Price for Food = ",market["Food"])
        print("Price for Tech = ",market["Tech"])
        print("**********************************************************")
        userInput = input("Enter 1 for Food, 2 for Tech or x for exit:")
        str =""
        if (userInput == "1"):
            str = "Food"
        elif(userInput == "2"):
            str= "Tech"
        else:
            break
        print("**********************************************************")
        max = 0
        if(market[str]*player.freeCargoUnits <= player.getCredits()):#enough credit?
            max = player.freeCargoUnits
        else:
            max = int(player.getCredits()/market[str])
        print("Price for "+str+" = ",market[str])
        secondInput = input("Would you like to buy (enter b) or sell (enter s)?")
        if (secondInput == "b"):#buying
            print("You can buy a maximum of",max,"units")
            nr = input("How much would you like to buy? Or press x to exit")
            if (nr == "x"):
                pass
            else:
                nr = int(nr)
                if((player.getCredits() > market[str]*nr) and (nr <= max)): #has enough money and space
                    if (str == "Food"):
                        player.addFood(nr)
                    else:
                        player.addTech(nr)
                    player.setCredits(player.getCredits() - market[str]*nr)
                    player.updateCargoUnits()
        else:#selling
            if (str == "Food"):
                print("You can sell a maximum of",player.getFood(),"food units")
                nr = input("How much would you like to sell? Or press x to exit")
                if (nr == "x"):
                    pass
                else:
                    nr = int(nr)
                    if (nr <= player.getFood()):
                        player.sellFood(nr)
                        player.setCredits(player.getCredits() + nr*market["Food"])
            else:
                print("You can sell a maximum of",player.getTech(),"tech units")
                nr = input("How much would you like to sell? Or press x to exit")
                if (nr == "x"):
                    pass
                else:
                    nr = int(nr)
                    if (nr <= player.getTech()):
                        player.sellTech(nr)
                        player.setCredits(player.getCredits() + nr*market["Tech"])
                
                
                              
    
def menu(player):
    global turnCounter
    notFinished = True
    planet = Planet.Planet(random.randint(1,3))
    while notFinished:#main game loop  
        cleanScreen()
        if (player.getCredits() < 0):
            print("Sorry, but you ran out of credits and therefore lost the game in round,",turnCounter,"!")
            break
        print("**********************************************************")
        print("Turn nr.",turnCounter,"in this glorious space trading simulation")
        player.printStats()
        print("**********************************************************")
        print("You are on Planet:",planet.getName())
        print("**********************************************************")
        print("Enter 1 to go to the shipyard")
        print("Enter 2 to go to the market")
        print("Enter 3 to go to the spaceport")
        print("Enter exit to leave the game")
        userinput = input("Your Input:")
        if (userinput == "1"):
            shipyardMenu(player, planet)
        elif (userinput == "2"):
            marketMenu(player, planet)
        elif (userinput == "3"):
            planet = spacePortMenu(player, planet)
        else:        
            notFinished = False
        
    
        

print("***************************************")
print("         Welcome to StarSim")
print("***************************************")
name = input("Please enter your Name:")
player = Player.Player(name)
menu(player)





