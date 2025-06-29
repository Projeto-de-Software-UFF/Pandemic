from controller.game_map_controller import GameMap

def viewMap():
    print('..................................')
    print('.......... Mapa do Jogo ..........')
    print('..................................')

    map = GameMap()
    for cidade in map.getMap():
        print(cidade.nome, end=" <-> ")
    print()
    print('..................................')
