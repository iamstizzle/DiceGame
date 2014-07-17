
################################### SETUP ###########################################################

from random import randint
import time

def d6():
    return randint(1,6)

### DICE TABLES ####

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

##----------------

### PLAYER SETUP ###

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

endscore = int(input("\nHow many Brain do you want to play to?: "))
print ("you've selected ", endscore)


            ###############  PLAY START ################

    ##Player setup##

player1 = dicerules("Player 1")
player2 = dicerules("Player 2")
player3 = dicerules("Player 3")
player4 = dicerules("Player 4")
computerai = dicerules("AI")

if playercount == 1:
    playerarray = [player1,computerai]
elif playercount == 2:
    playerarray = [player1,player2]
elif playercount ==3:
    playerarray = [player1,player2, player3]
elif playercount ==4:
    playerarray = [player1,player2, player3, player4]
    

### Mechanics of each turn ###
while player1.totalbrains < endscore and player2.totalbrains < endscore and player3.totalbrains < endscore and computerai.totalbrains < endscore and player4.totalbrains < endscore:

    for each in playerarray:
        
        scorepoints = False

        ### PLAYER 1  ###
        print ("\n", each.name,"START:\nDrawing DIE ...er, dice... \n")
        each.fillhand()                                                                 
        each.handroll()
        each.checkroll()
        print (each.name, " your roll was :", each.rolled[0][0], each.rolled[1][0], each.rolled[2][0])
        print ("\nRoll results for ", each.name, "\nBrains: ", each.brains, " Shotgun: ", each.shotguncount, "\n\n\n\n")


        while each.shotguncount <3 and scorepoints == False:
            scorepoints = False
            if each.shotguncount < 3:
                ### AI section ###
                ### rules determining rerolls for AI  and player type###
                if each.name == "AI":
                    if each.brains ==0:
                        question = str("y")
                    elif player1.totalbrains >= endscore and (computerai.totalbrains + computerai.brains) < player1.totalbrains:
                        question = str("y")
                    elif player1.totalbrains < endscore and (computerai.totalbrains + computerai.brains) >= endscore:
                        question = str("n") ## should stop if you have the win
                    elif computerai.brains <6 and computerai.shotguncount == 0:
                        question = str("y")
                        time.sleep(1)
                    elif computerai.brains <3 and computerai.shotguncount == 1:
                        if randint(1,10) < 10:
                            ##adding some randomness to ai
                            question = str("y")
                            time.sleep(5)
                        else:
                            question = str("n")
                    elif computerai.brains <5 and computerai.shotguncount <3:
                        if d6() < 5:
                            ##adding some randomness to ai
                            question = str("y")
                        else:
                            question = str("n")
                    else:
                        question = str("n")
                        #### end AI   
                ## else you are human input prompt ##
                else:
                    question = str(input("reroll?: " ))
                    
            
                if question =="y":
                    print("rerolling")
                    each.fillhand()
                    #print ("you drew out: ", each.hand, "\nRemaining to draw from bucket ", each.bucket)
                    each.handroll()
                    each.checkroll()
                    #print ("your roll was :", each.rolled[0][0], each.rolled[1][0], each.rolled[2][0])
                    print (each.name, " roll totals:\n--- Brains: ", each.brains, "\n--- Shotgun: ", each.shotguncount, "\n\n\n")
                    time.sleep(1)
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

        ### End human controlled input prompts###
        time.sleep(2)
    print ("Current game standings are:")
    time.sleep(1)
    for each in playerarray:
        print ("\n", each.name, " brains in the brain bank ", each.totalbrains, "\n------------\n")
        time.sleep(2)



### For loop removal ###
##Game end resets ###

player1.reset()
player2.reset()
player3.reset()
computerai.reset()

############################ VICTORY CONDITIONS MET  #########################################3

winner = [["name",0]]

for each in playerarray:
    #print ("Victory condition debug print", winner[0], winner[0][1])
    if each.totalbrains > winner[0][1]:
        winner =[[each.name, each.totalbrains]]
    
time.sleep(2)

print ("\nThe Winner is: ", winner[0][0], " with ", winner[0][1], " brains!")
### I  dont yet account for ties. ### needs fixing  and support more than 2 players.

print ("exiting");
time.sleep(1)
print (".");
time.sleep(1)
print (".");
time.sleep(1)

### AI_tweakbranch ####
