#!/usr/bin/env python
box = 0
playAgain = 1
print "Boxes!"
box = int(raw_input("Open one? Type a number."))
while playAgain == 1:
    while box != 0:
        print "You acutally opened one? Wow, you deserve a medal!"
        playAgain = int(raw_input("Are you done yet? Type 1 for no and any other number for yes."))
        box = 0
