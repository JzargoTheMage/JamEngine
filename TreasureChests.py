#!/usr/bin/env python
box = 0
playAgain = 1
print "Treasure!"
while playAgain == 1:
    box = int(raw_input("Open one? Type a number."))
    if box != 0:
        print "You acutally opened one? You have no life."
        playAgain = int(raw_input("Are you done yet? Type 1 for no and any other number for yes."))
        box = 0
