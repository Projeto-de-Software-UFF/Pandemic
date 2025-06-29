from controller.game_map_controller import GameMap

def exibir_mapa(mapa):
    for cidade in mapa:
        vizinhos = [vizinho.nome for vizinho in cidade.vizinhacidade]
        print(f"Cidade: {cidade.nome} -> Vizinhos: {', '.join(vizinhos)}")

if __name__ == "__main__":
    mapa = GameMap().getMap()
    exibir_mapa(mapa)