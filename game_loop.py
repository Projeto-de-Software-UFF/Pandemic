from terminal_view.header import header
from terminal_view.menu import menu
from terminal_view.painel import painel

while True:
    header()
    painel()
    menu()

    opcao = int(input('Digite sua ação: '))

    if opcao == 0:
        break
