
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

player = dicerules()
player2 = dicerules()
player3 = dicerules()
##development mode##
computerai = dicerules()



while player.totalbrains < 13 and player2.totalbrains < 13 and computerai.totalbrains < 13:
    scorepoints = False

    ### PLAYER 1  ###
    print ("PLAYER 1 START:\nDrawing DIE ...er, dice... \n")
    player.fillhand()
    #print ("you drew out: ", player.hand, "\nRemaining to draw from bucket ", player.bucket, "\n\n\n")                                                                     

    player.handroll()
    player.checkroll()
    print ("your roll was :", player.rolled[0][0], player.rolled[1][0], player.rolled[2][0])
    print ("player 1 roll totals:  Brains: ", player.brains, "Shotgun: ", player.shotguncount, "\n\n\n\n")


    while player.shotguncount <3 and scorepoints == False:
        scorepoints = False
        if player.shotguncount < 3:
            question = str(input("reroll?: " ))
            if question =="y":
                print("rerolling")
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
    if playercount >= 2:  ##adds multiplayer
        scorepoints = False   #need so you can enter the dice reroll while loop
        print ("Player2 START:\nDrawing DIE ...er, dice... \n")
        time.sleep(1)
        player2.fillhand()
        #print ("P2 you drew out: ", player2.hand, "\nRemaining to draw from bucket ", player2.bucket)
                                                                                     

        player2.handroll()
        player2.checkroll()
        print ("your roll was :", player2.rolled[0][0], player2.rolled[1][0], player2.rolled[2][0])
        print ("player 2 roll totals:  Brains: ", player2.brains, "Shotgun: ", player2.shotguncount, "\n\n\n\n")
 
        while player2.shotguncount <3 and scorepoints == False:
            scorepoints = False
            if player2.shotguncount < 3:
                question = str(input("reroll?: " ))
                if question =="y":
                    print("rerolling")
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
        player2.reset()

        time.sleep(2)
        if playercount == 2:
            print ("\n\n\n---End of Round---\nHere are the scores:\nPlayer 1 has ", player.totalbrains, "\nand Player 2 has " , player2.totalbrains, "\n--------------------------------\n\n")
        time.sleep(3)

### Add extra players:


    ###PLAYER 3 ###
    if playercount > 2:
        
        scorepoints = False   #need so you can enter the dice reroll while loop
        print ("Player 3 START:\nDrawing DIE ...er, dice... \n")
        time.sleep(1)
        player3.fillhand()
        #print ("P2 you drew out: ", player2.hand, "\nRemaining to draw from bucket ", player2.bucket)
                                                                                     

        player3.handroll()
        player3.checkroll()
        print ("your roll was :", player3.rolled[0][0], player3.rolled[1][0], player3.rolled[2][0])
        print ("player 2 roll totals:  Brains: ", player3.brains, "Shotgun: ", player3.shotguncount, "\n\n\n\n")

            
        while player3.shotguncount <3 and scorepoints == False:
            scorepoints = False
            if player3.shotguncount < 3:
                question = str(input("reroll?: " ))
                if question =="y":
                    print("rerolling")
                    player3.fillhand()
                    print ("you drew out: ", player3.hand, "\nRemaining to draw from bucket ", player3.bucket)
                    player3.handroll()
                    player3.checkroll()
                    print ("your roll was :", player3.rolled[0][0], player3.rolled[1][0], player3.rolled[2][0])
                    print ("player 1 roll totals:  Brains: ", player3.brains, "Shotgun: ", player3.shotguncount, "\n\n\n\n")

                elif question =="n":
                    scorepoints = True
                    player3.totalbrains += player3.brains
                    player3.reset()        

        player3.reset()
        print ("brains in the brain bank ", player3.totalbrains)

        if playercount == 3:
            print ("\n\n\n---End of Round---\nHere are the scores:\nPlayer 1 has ", player.totalbrains, "\nand Player 2 has " , player2.totalbrains, "\n\n\n\nand Player 3 has " , player3.totalbrains, "\n---------------\n\n")

        


###ai demo###################################################3
            ##################3333
            ##################




    if playercount == 1:
            
            scorepoints = False   #need so you can enter the dice reroll while loop
            print ("AI PLAYER START:\nDrawing DIE ...er, dice... \n")
            time.sleep(1)
            computerai.fillhand()
            #print ("COMPUTER you drew out: ", player2.hand, "\nRemaining to draw from bucket ", player2.bucket)
                                                                                         

            computerai.handroll()
            computerai.checkroll()
            print ("your roll was :", computerai.rolled[0][0], computerai.rolled[1][0], computerai.rolled[2][0])
            print ("player 2 roll totals:  Brains: ", computerai.brains, "Shotgun: ", computerai.shotguncount, "\n\n\n\n")

                
            while computerai.shotguncount <3 and scorepoints == False:
                scorepoints = False
                if computerai.shotguncount < 3:


### try to add aI rules
                    if computerai.brains == 0:
                        question = str("y")
                    elif computerai.brains <7 and computerai.shotguncount == 0:
                        question = str("y")
                    elif computerai.brains <3 and computerai.shotguncount == 1:
                        if d6() < 6:
                            ##adding some randomness to ai
                            question = str("y")
                        else:
                            question = str("n")
                    elif computerai.brains <6 and computerai.shotguncount <3:
                        if d6() < 5:
                            ##adding some randomness to ai
                            question = str("y")
                        else:
                            question = str("n")
                    else:
                        question = str("n")
                        
                            
                        



                    
                    if question =="y":
                        print("rerolling")
                        computerai.fillhand()
                        print ("you drew out: ", computerai.hand, "\nRemaining to draw from bucket ", computerai.bucket)
                        computerai.handroll()
                        computerai.checkroll()
                        print ("your roll was :", computerai.rolled[0][0], computerai.rolled[1][0], computerai.rolled[2][0])
                        print ("Computer roll totals:  Brains: ", computerai.brains, "Shotgun: ", computerai.shotguncount, "\n\n\n\n")

                    elif question =="n":
                        scorepoints = True
                        computerai.totalbrains += computerai.brains
                        computerai.reset()        

            computerai.reset()
            print ("COMPUTER brains in the brain bank ", computerai.totalbrains, "\n\n\n")




################ END AI TEST####################################



player.reset()
player2.reset()
player3.reset()
computerai.reset()









print ("\n\n\nVICTORY!!!:\nPlayer 1 has ", player.totalbrains, "\nand Player 2 has " , player2.totalbrains)
















if player.totalbrains > player2.totalbrains:
    print("Player 1 wins!")
else:
    print ("player 2 wins")

### I  dont yet account for ties. ### needs fixing  and support more than 2 players.
          

######dietest########


print ("exiting");
time.sleep(1)
print (".");
time.sleep(1)
print (".");
time.sleep(1)
print (".")


