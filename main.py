from entities import player
from resources import material, tool


player1 = player.Player("Sancho")
wooden_pickaxe = tool.WoodenPickaxe()
player1.equip(wooden_pickaxe)
print(player1)

stone = material.Stone()
print(stone)
stone.breaking(player1)
print(player1)
print(stone)

player2 = player.Player("Cold_x")
print(player2)
concrete = material.Concrete()
print(concrete)
concrete.breaking(player2)
print(concrete)
print(player2)

iron = material.Iron()
print(iron)
iron.breaking(player2)
print(player2)
print(iron)
iron_pickaxe = tool.IronPickaxe()
player2.equip(iron_pickaxe)
print(player2)
iron.breaking(player2)
print(player2)
print(iron)
