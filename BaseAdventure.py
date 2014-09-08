#!/usr/bin/env python
print "Welcome!"
Area = 0
Health = 10
Attack = 3
Defense = 5
enemyHealth = 0
enemyAttack = 0
enemyDefense = 0
damage = 0
battleAction = 0
OriginalHealth = 0
OriginalAttack = 0
OriginalDefense = 0
TempAttack = 0
TempDefense = 0
enemyType = 0
playerType = 0
battleStatus = "None"
enemyName = "None"
poison = False
enemyPoison = False
Coins = 15
ShopMenu = 0
playAgain = 1

#Defined actions are below

#Battle is self-explanatory, set of commands for encounters

def Battle():
    global battleAction
    print "Enemy Name: ", enemyName
    print "Enemy Health: ", enemyHealth
    print "Your Health: ", Health
    while battleAction == 0:
        battleAction = int(raw_input("Enter 1 to attack, 2 to defend, or 3 to attack with poison.  "))
    while battleAction == 1:
        Attacking()
        if battleStatus == "None":
            EnemyAttacking()
        PoisonCheck()
        battleAction = 0
    while battleAction == 2:
        Defending()
        if battleStatus == "None":
            EnemyAttacking()
        ReturnDefense()
        PoisonCheck()
        battleAction = 0
    while battleAction == 3:
        PoisonAttacking()
        if battleStatus == "None":
            EnemyAttacking()
        PoisonCheck()
        battleAction = 0

#Function to check for victory

def CheckVictory():
    global battleStatus
    if enemyHealth <= 0:
        battleStatus = "Victory"
        Victory()

#Function to check for defeat

def CheckDefeat():
    global battleStatus
    if Health <= 0:
        battleStatus = "Defeat"
        Defeat()

#Poisonous version of Attack and vice versa 

def PoisonAttacking():
    global enemyHealth
    global damage
    global Attack
    global OriginalAttack
    global enemyPoison
    OriginalAttack = Attack
    Attack /= 2
    damage = Attack - enemyDefense
    enemyHealth -= damage
    enemyPoison = True
    print "You successfully poisoned the", enemyName, "!"
    print "The", enemyName, "takes", damage, "points of damage!"
    Attack = OriginalAttack
    damage = 0
    OriginalAttack = 0
    CheckVictory()

def EnemyPoisonAttacking():
    global Health
    global damage
    global enemyAttack
    global OriginalAttack
    global poison
    OriginalAttack = enemyAttack
    enemyAttack /= 2
    damage = enemyAttack - Defense
    Health -= damage
    poison = True
    print "The", enemyName, "successfully poisoned you!"
    print "You take", damage, "points of damage!"
    enemyAttack = OriginalAttack
    damage = 0
    CheckDefeat()

#Function for poison damage

def PoisonCheck():
    global Health
    global enemyHealth
    global poison
    if poison == True:
        Health = Health - 2
        print "You are damaged by poison!"
        CheckDefeat()
    if enemyPoison == True:
        enemyHealth = enemyHealth - 2
        print "The", enemyName, "is damaged by poison!"
        CheckVictory()

#Attacking puts Attack vs. enemyDefence and vice versa
        
def Attacking():
    global enemyHealth
    global damage
    damage = Attack - enemyDefense
    NegativeDamage()
    enemyHealth = enemyHealth - damage
    print "You attack the", enemyName, "!"
    print enemyName, "takes ", damage, " points of damage!"
    CheckVictory()
    damage = 0

def EnemyAttacking():
    global Health
    global damage
    damage = enemyAttack - Defense
    NegativeDamage()
    Health = Health - damage
    print "The", enemyName, "attacks!"
    print "You took ", damage, " points of damage!"
    CheckDefeat()
    damage = 0

#Defending doubles Defense in exchange for the user's attack that turn (temp.)

def Defending():
    global Defense
    global Health
    global damage
    OriginalDefense = Defense
    Defense = Defense * 2
    print "You are guarding!"

def ReturnDefense():
    Defense = OriginalDefense

#This ensures that the user does not gain Health from being attacked
    
def NegativeDamage():
    global damage
    if damage < 0:
        damage = 0

#This is the testing user class. As named, it is over powered.
#Make other classes based on this template

def OP():
    global Health
    global Attack
    global Defense
    Health = 20
    Attack = 20
    Defense = 20

#This is the generic nameless enemy template
#Base other enemies off of this template
    
def EasyFiller():
    global enemyName
    global enemyHealth
    global enemyAttack
    global enemyDefense
    enemyName = "EasyFiller"
    enemyHealth = 5
    enemyAttack = 5
    enemyDefense = 5

def MediumFiller():
    global enemyName
    global enemyHealth
    global enemyAttack
    global enemyDefense
    enemyName = "MediumFiller"
    enemyHealth = 10
    enemyAttack = 10
    enemyDefense = 10

#This states the actions to follow for a successful battle (conditions in battle def.)
    
def Victory():
    global battle
    global playerType
    global enemyType
    global poison
    global enemyPoison
    global playAgain
    print "You were victorious against", enemyName, "!"
    battle = False
    playerType = 0
    enemyType = 0
    poison = False
    enemyPoison = False
    playAgain = int(raw_input("Try another battle? Type 1 for yes, or any other number to quit.  "))

#This states the actions to follow for a lost battle (conditions in battle def.)

def Defeat():
    global battle
    global playerType
    global enemyType
    global poison
    global enemyPoison
    global playAgain
    print "You were defeated by", enemyName, "!"
    battle = False
    playerType = 0
    enemyType = 0
    poison = False
    enemyPoison = False
    playAgain = int(raw_input("Try another battle? Type 1 for yes, or any other number to quit.  "))

#Beginning of main program, need to integrate the above actions into below game still
#Start working here.
#Or else.
#I'm watching me.
#Integrate Class choice and make temp and original variables work.

while playAgain == 1:
    while Area == 0:
        print "What would you like to do?"
        Area = int(raw_input("Type 1 to go shopping, or 2 to proceed on your journey.  ")
    while Area == 1:
        if ShopMenu == 0:
            print "Welcome to the shop! What would you like? Upgrades are 5 coins."
            ShopMenu = int(raw_input("1 is Attack, 2 is Defense, 3 is Health. Type 4 to return to town center.  ")
        if ShopMenu == 1:
            Attack = Attack + 2
            ShopMenu = 0
        if ShopMenu == 2:
            Defense = Defense +2
            ShopMenu = 0
        if ShopMenu == 3:
            Health = Health +5
            ShopMenu = 0
        if ShopMenu == 4:
            Area = 0
            ShopMenu = 0
    while Area == 2:
        print "Go away."
        Area = 0
#Need to add the battle and treasure options into this
