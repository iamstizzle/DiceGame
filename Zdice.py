
################################### SETUP ###########################################################
from random import randint
import time


def d6():
    return randint(1,6)
#--------------------------


##### DEFINE Dictionary of Dice values ###

dieval = {
    "civi1" : ["shotgun","reroll","reroll","brains","brains","brains"],
    "civi2" : ["shotgun","reroll","reroll","brains","brains","brains"],
    "civi3" : ["shotgun","reroll","reroll","brains","brains","brains"],
    "civi4" : ["shotgun","reroll","reroll","brains","brains","brains"],
    "civi5" : ["shotgun","reroll","reroll","brains","brains","brains"],
    "civi6" : ["shotgun","reroll","reroll","brains","brains","brains"],
    "mili7": ["shotgun","shotgun", "reroll","reroll","brains","brains"],
    "mili8" : ["shotgun","shotgun", "reroll","reroll","brains","brains"],
    "mili9" : ["shotgun","shotgun", "reroll","reroll","brains","brains"],
    "army10" : ["shotgun","shotgun", "shotgun","reroll","reroll","brains"],
    "army11" : ["shotgun","shotgun", "shotgun","reroll","reroll","brains"],
    "pro12" : ["shotgun", "shotgun", "dubshotgun", "reroll","brains","dubbrains"],

    }

#Test Dice rolls for dict values
#####------------------------------------------------------------------


#####Define Draw bucket#####
##!!!! note array == []    dictionary == {}##


class dicerules(object):
    def __init__(self):
        self.bucket = [
            "civi1",
            "civi2",
            "civi3",
            "civi4",
            "civi5",
            "civi6",
            "mili7",
            "mili8",
            "mili9",
            "army10",
            "army11",
            "pro12"
            ]
        self.useddice = []
        self.hand = []
        self.totalbrains = 0
        self.brains = 0
        self.shotguncount = 0
        
    def reset(self):
        self.bucket = [
            "civi1",
            "civi2",
            "civi3",
            "civi4",
            "civi5",
            "civi6",
            "mili7",
            "mili8",
            "mili9",
            "army10",
            "army11",
            "pro12"
            ]
        self.useddice = []
        self.hand = []
        self.shotguncount = 0
        self.brains = 0
    def addpoint(self, points):
        self.brains += points
    def gotshot(self, shot):
        self.shotguncount += shot

    def fillhand(self):
        #Draw from bucket until you have 3
        #debug#print ("hand length ", len(self.hand))
        while len(self.hand) < 3:
            ##prevent draw error from empty bucket
            if len(self.bucket) < 1:
                self.bucket = self.useddice
            ## grab 1 random die from bucket, add it to hand, and remove from bucket
            getdie = randint(0,len(self.bucket)-1)
            """ migh need an index of 0 for randint start """
            self.hand.append(self.bucket[getdie])
            self.bucket.remove(self.bucket[getdie])
            ########print ("\n\n TEST HAND TEST hand", self.hand, " diebucket", self.bucket)
            ##WARNING  need to add code to reset bucket but not hand
            ## If the bucket contains fewer dice than needs to be drawn.
            
    def handroll(self):
        self.rolled = []
        if len(self.hand) == 3:

            ## maybe append in tuples of roll value and dice value @#@#@#@#@#!@#!@#!@#!@#!@#
            self.rolled = [[dieval[self.hand[0]][d6()-1],self.hand[0]], [dieval[self.hand[1]][d6()-1],self.hand[1]], [dieval[self.hand[2]][d6()-1],self.hand[2]] ]
            #debug#print ("#####", self.rolled, "\nindex0", self.rolled[0], "\nindex0", self.rolled[0][0], "print hand", self.hand, "\nindex0 diceval1: ", self.rolled[0][1] )
            
        else:
            print ("you dont have enough dice")

    def checkroll(self):
      for each in self.rolled:
            #print (each[1])
            if each[0] == "shotgun":
                self.gotshot(1)
                ## remove dice
                self.useddice.append(each[1])
                self.hand.remove(each[1])
            elif each[0] == "brains":
                self.addpoint(1)
                ## remove dice
                self.useddice.append(each[1])
                self.hand.remove(each[1])
            elif each[0] == "reroll":
                uselessvar = True
            elif each[0] == "dubbrains":
                self.addpoint(2)
                ## remove dice
                self.useddice.append(each[1])
                self.hand.remove(each[1])
            elif each[0] == "dubshotgun":
                self.gotshot(2)
                self.useddice.append(each[1])
                self.hand.remove(each[1])
                ### may need a better way to know what is where on the roll so rerolls stay in hand."""
               
                
 ## delete self.hand[self.hand[0]]
                ## might remove unwanted element from an array
                # may have to rename values in array to string for each dice from self.bucket. instead of 1,2,3  to "civ","militia", "army"
        
#----------------------------------------------------------------------------------
            
################################### SETUP END ###########################################################

#----------------------------------------------------------------------

### define die role rules/values/turn end condition###
""" setup for multiple players  will go here """
""" Checks for victory conditions will go here"""
    #######################################################




            ###############  PLAY START ################

    ##Player setup##

player = dicerules()
player2 = dicerules()



###setup for multiplayer loop checks..
while player.totalbrains < 13 and player2.totalbrains < 13:
    scorepoints = False

    ### PLAYER 1  ###
    print ("PLAYER 1 START:\nDrawing DIE ...er, dice... \n")
    player.fillhand()
    print ("you drew out: ", player.hand, "\nRemaining to draw from bucket ", player.bucket, "\n\n\n")                                                                     

    player.handroll()
    player.checkroll()
    print ("your roll was :", player.rolled[0][0], player.rolled[1][0], player.rolled[2][0])
    print ("player 1 roll totals:  Brains: ", player.brains, "Shotgun: ", player.shotguncount, "\n\n\n\n")


    while player.shotguncount <3 and scorepoints == False:
        scorepoints = False
        if player.shotguncount < 3:
            question = str(input("reroll?: " ))
            print("rerolling")
            if question =="y":
                player.fillhand()
                print ("you drew out: ", player.hand, "\nRemaining to draw from bucket ", player.bucket)
                player.handroll()
                player.checkroll()
                print ("your roll was :", player.rolled[0][0], player.rolled[1][0], player.rolled[2][0])
                print ("player 1 roll totals:  Brains: ", player.brains, "Shotgun: ", player.shotguncount, "\n\n\n\n")

            elif question =="n":
                scorepoints = True
                player.totalbrains += player.brains
                player.reset()        

    player.reset()
    print ("brains in the brain bank ", player.totalbrains, "\n\n--------------------------------\n\n") 
    player.reset() #these resets are important to avoid comingling values for future turns.

    ### End player 1
    time.sleep(2)

    ###start player 2
    scorepoints = False   #need so you can enter the dice reroll while loop
    print ("Player2 START:\nDrawing DIE ...er, dice... \n")
    time.sleep(1)
    player2.fillhand()
    print ("P2 you drew out: ", player2.hand, "\nRemaining to draw from bucket ", player2.bucket)
                                                                                 

    player2.handroll()
    player2.checkroll()
    print ("your roll was :", player2.rolled[0][0], player2.rolled[1][0], player2.rolled[2][0])
    print ("player 2 roll totals:  Brains: ", player2.brains, "Shotgun: ", player2.shotguncount, "\n\n\n\n")

        
    while player2.shotguncount <3 and scorepoints == False:
        scorepoints = False
        if player2.shotguncount < 3:
            question = str(input("reroll?: " ))
            print("rerolling")
            if question =="y":
                player2.fillhand()
                print ("you drew out: ", player2.hand, "\nRemaining to draw from bucket ", player2.bucket)
                player2.handroll()
                player2.checkroll()
                print ("your roll was :", player2.rolled[0][0], player2.rolled[1][0], player2.rolled[2][0])
                print ("player 1 roll totals:  Brains: ", player2.brains, "Shotgun: ", player2.shotguncount, "\n\n\n\n")

            elif question =="n":
                scorepoints = True
                player2.totalbrains += player2.brains
                player2.reset()        

    player2.reset()
    print ("brains in the brain bank ", player2.totalbrains) 
    print ("blasted! turn over")

    player2.reset()

    time.sleep(2)
    print ("\n\n\nEnd of turn BLAH, here are the scores:\nPlayer 1 has ", player.totalbrains, "\nand Player 2 has " , player2.totalbrains, "\n\n--------------------------------\n\n")
    time.sleep(3)

player.reset()
player2.reset()

print ("\n\n\nVICTORY!!!:\nPlayer 1 has ", player.totalbrains, "\nand Player 2 has " , player2.totalbrains)

if player.totalbrains > player2.totalbrains:
    print("Player 1 wins!")
else:
    print ("player 2 wins")

### I  dont yet account for ties. ### needs fixing.
          

######dietest########


print ("exiting");
time.sleep(1)
print (".");
time.sleep(1)
print (".");
time.sleep(1)
print (".")


