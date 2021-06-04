from mcpi import block
from mcpi.minecraft import Minecraft

game = Minecraft.create(port=4711)
game.setBlock(50, 50, 50, "minecraft:dirt")
# game.postToChat('hi')
