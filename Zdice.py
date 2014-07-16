
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
    def __init__(self, title):
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
        self.name = title
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
        while len(self.hand) < 3:
            ##prevent draw error from empty bucket
            if len(self.bucket) < 1:
                self.bucket = self.useddice
                self.useddice = []
            ## grab 1 random die from bucket, add it to hand, and remove from bucket
            getdie = randint(0,len(self.bucket)-1)
            """ migh need an index of 0 for randint start """
            self.hand.append(self.bucket[getdie])
            self.bucket.remove(self.bucket[getdie])
            
    def handroll(self):
        self.rolled = []
        if len(self.hand) == 3:
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
               
        
#----------------------------------------------------------------------------------
            
################################### SETUP END ###########################################################

#----------------------------------------------------------------------

playercount = int(input("--Zombie Dice--\n\nHow many players: " ))
print ("you've selected ", playercount)

            ###############  PLAY START ################

    ##Player setup##

player1 = dicerules("player 1")
player2 = dicerules("player 2")
player3 = dicerules("player 3")
player4 = dicerules("player 4")
##development mode##
computerai = dicerules("AI")

if playercount == 1:
    playerarray = [player1,computerai]
elif playercount == 2:
    playerarray = [player1,player2]
elif playercount ==3:
    playerarray = [player1,player2, player3]
elif playercount ==4:
    playerarray = [player1,player2, player3, player4]
    


while player1.totalbrains < 13 and player2.totalbrains < 13 and player3.totalbrains < 13 and computerai.totalbrains < 13 and player4.totalbrains < 13:

    for each in playerarray:
        
        scorepoints = False

        ### PLAYER 1  ###
        print ("\n", each.name,"START:\nDrawing DIE ...er, dice... \n")
        each.fillhand()
        #print ("you drew out: ", each.hand, "\nRemaining to draw from bucket ", player.bucket, "\n\n\n")                                                                     

        each.handroll()
        each.checkroll()
        print ("\n", each.name, " your roll was :", each.rolled[0][0], each.rolled[1][0], each.rolled[2][0])
        print ("playername", each.name, " roll totals:  Brains: ", each.brains, "Shotgun: ", each.shotguncount, "\n\n\n\n")


        while each.shotguncount <3 and scorepoints == False:
            scorepoints = False
            if each.shotguncount < 3:
            ### AI section ##
                if each.name == "AI":
                    if each.brains ==0:
                        question = str("y")
                    elif player1.totalbrains > 12 and (computerai.totalbrains + computerai.brains) < player1.totalbrains:
                        question = str("y")
                    elif computerai.brains <7 and computerai.shotguncount == 0:
                        question = str("y")
                        time.sleep(1)
                    elif computerai.brains <3 and computerai.shotguncount == 1:
                        if randint(1,8) < 8:
                            ##adding some randomness to ai
                            question = str("y")
                            time.sleep(1)
                        else:
                            question = str("n")
                    elif computerai.brains <5 and computerai.shotguncount <3:
                        if d6() < 4:
                            ##adding some randomness to ai
                            question = str("y")
                        else:
                            question = str("n")
                    else:
                        question = str("n")
                ## else you are human input prompt.
                else:
                    question = str(input("reroll?: " ))
                    
#### end AI


            
            
                if question =="y":
                    print("rerolling")
                    each.fillhand()
                    print ("you drew out: ", each.hand, "\nRemaining to draw from bucket ", each.bucket)
                    each.handroll()
                    each.checkroll()
                    print ("your roll was :", each.rolled[0][0], each.rolled[1][0], each.rolled[2][0])
                    print ("player ", each.name, " roll totals:  Brains: ", each.brains, "Shotgun: ", each.shotguncount, "\n\n\n\n")

                elif question =="n":
                    scorepoints = True
                    each.totalbrains += each.brains
                    each.reset()        

        if each.shotguncount > 2:
            print ("\nBoom! The undead don't unlive forever. You got blasted!\n")
            time.sleep(1)
        each.reset()
        print ("brains in the brain bank ", each.totalbrains, "\n\n--------------------------------\n\n") 
        each.reset() #these resets are important to avoid comingling values for future turns.

        ### End player 1###
        time.sleep(2)
    print ("Current game standings are:")
    time.sleep(1)
    for each in playerarray:
        print ("\nplayer: ", each.name, " brains in the brain bank ", each.totalbrains, "\n--------------\n")



### For loop removal ###





    ### For loop end

player1.reset()
player2.reset()
player3.reset()
computerai.reset()



############################ VICTORY CONDITIONS MET  #########################################3


###messed up for computerai as player 2""
if playercount == 1:
    print ("\n\n\nVICTORY!!!:\nPlayer 1 has ", player1.totalbrains, "\nand the Computer has " , computerai.totalbrains)
    if player1.totalbrains > computerai.totalbrains:
        print("Player 1 wins!")
    else:
        print ("Computer wins")

elif playercount == 2:
    print ("\n\n\nVICTORY!!!:\nPlayer 1 has ", player1.totalbrains, "\nand Player 2 has " , computerai.totalbrains)
    if player1.totalbrains > computerai.totalbrains:
        print("Player 1 wins!")
    else:
        print ("Computer wins")

elif playercount == 3:
    print ("\n\n\nVICTORY!!!:\nPlayer 1 has ", player1.totalbrains, "\nand Player 2 has " , player2.totalbrains, "\nand Player 3 has " , player3.totalbrains)
    if player1.totalbrains > player2.totalbrains and player1.totalbrains > player3.totalbrains:
        print("Player 1 wins!")
    elif player1.totalbrains < player2.totalbrains and player2.totalbrains > player3.totalbrains:
        print ("Player 2 wins")
    else: print ("Player 3 wins")

else:
    print ("this shouldn't happen and I dont yet break ties. ties always go to player 3.")



### I  dont yet account for ties. ### needs fixing  and support more than 2 players.
######dietest########


print ("exiting");
time.sleep(1)
print (".");
time.sleep(1)
print (".");
time.sleep(1)

### Cleanbranch multiplayer line commit ####
