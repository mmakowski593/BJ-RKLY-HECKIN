from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

name = ""
scoreboard = {}

while True:
    name = input("what is your name? ")
    if name == "exit":
        break
    mc.postToChat("BJORKLY")    
    time.sleep(60)

    blockHits = mc.events.pollBlockHits()

    blockHitsLength = len(blockHits)
    mc.postToChat("Your score is " + str(blockHitsLength))
    scoreboard[name] = len(blockHits)
    print(scoreboard)
