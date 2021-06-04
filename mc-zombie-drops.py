from mcpi import block
from mcpi.minecraft import Minecraft

game = Minecraft.create()
game.postToChat('hi')
print(game.getBlockWithData(68, 64, 258))
game.setBlock(67, 64, 257, block.DIAMOND_BLOCK.id)


