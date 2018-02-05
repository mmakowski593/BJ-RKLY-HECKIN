from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = 35
state = 6

def getwoolstate(color):
    if color == 'pink':
        blockstate = 6

    if color == 'white':
        blockstate = 0

    if color == 'orange':
        blockstate = 1

    if color == 'magenta':
        blockstate = 2

    if color == 'yellow':
        blockstate = 4

    if color == 'light blue':
        blockstate = 3

    return blockstate
state = getwoolstate(input("Enter a block color"))
print ("nubbin")
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
