from controller.game_map_controller import GameMap

map = GameMap()
for cidade in map.getMap():
    print(cidade.nome, end=" <-> ")
