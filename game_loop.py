from terminal_view.header import header
from terminal_view.menu import menu
from terminal_view.painel import painel
from terminal_view.view_map import viewMap

turno = 0

while True:
    turno += 1
    header(turno)
    painel()
    menu()
    viewMap()
    
    opcao = int(input('Digite sua ação: '))

    if opcao == 0:
        break
