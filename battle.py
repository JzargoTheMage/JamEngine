#!/usr/bin/env python
enemyType = 0
enemyHealth = 0
enemyAttack = 0
enemyDefense = 0
battleOption = 0
damage = 0
Health = 20
Attack = 20
Defense = 20
battleAgain = 1
while battleAgain == 1:
    if enemyType == 0:
        print "What type of enemy do you want to face?"
        enemyType = int(raw_input("Type 1 to encounter an enemy.  ")
    if enemyType == 1:
        print "You encountered a filler enemy!"
        enemyHealth = 5
        enemyAttack = 5
        enemyDefense = 5
        if enemyHealth <= 0
            print "You felled the enemy!"
            battleAgain = int(raw_input("Battle again? Type 1 for yes, or any other number to exit.  ")
        if Health <= 0
            print "You were felled by the enemy!"
            battleAgain = int(raw_input("Try again? Type 1 for yes, or any other number to exit.  ")
        if battleOption == 0:
            battleOption = int(raw_input("Enter 1 to attack, or 2 to run.  ")
        if battleOption == 1:
            damage = Attack - enemyDefense
            enemyHealth -= damage
            print "The enemy took ", damage, "points of damage!"
            damage = 0
            damage = enemyAttack - Defense
            Health -= damage
#Add print for damage taken and current health.
