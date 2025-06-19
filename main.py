import curses
from layout_utils import dividir_tela_em_tres

def main(stdscr):
    # Desativa o cursor para não piscar na tela
    curses.curs_set(0)
    stdscr.keypad(True)

    # Definição de menus principais e submenus como mock-up
    menu_hierarchy = {
        "Mover": ["1. Para Cidade Vizinha", "2. Para Qualquer Cidade", "0. Voltar"],
        "Tratar Doença": ["1. Remover 1 Nível", "2. Remover Todos os Níveis (se Cura Descoberta)", "0. Voltar"],
        "Construir Centro Pesquisa": ["1. Construir Centro (custa 1 Ação)", "0. Voltar"],
        "Compartilhar Informação": ["1. Dar Carta", "2. Receber Carta", "0. Voltar"],
        "Descobrir Cura": ["1. Usar 4 Cartas da Mesma Cor", "0. Voltar"],
        "Bloquear Infecção": ["1. Selecionar Cidade Alvo", "0. Voltar"],
        "Remover Doença": ["1. Selecionar Cidade Alvo", "0. Voltar"],
        "Teletransporte": ["1. Escolher Jogador", "0. Voltar"],
        "Evento Doença": ["1. Revelar Cartas de Infecção", "0. Voltar"],
    }

    # Menu principal: última opção (0) será "Sair"
    main_menu = [
        "Mover",
        "Tratar Doença",
        "Construir Centro Pesquisa",
        "Compartilhar Informação",
        "Descobrir Cura",
        "Bloquear Infecção",
        "Remover Doença",
        "Teletransporte",
        "Evento Doença",
        "Sair"
    ]

    # Pilha que mantém o histórico de menus (para permitir voltar)
    menu_stack = [main_menu]
    # Texto fixo para a área central (mock-up)
    texto_central = "=== MicroPandemic ===\nTurno do Jogador\nSelecione uma ação no menu abaixo."
    # Mock-up de informações constantes na lateral direita
    texto_lateral = (
        "Jogador: Dr. Silva\n"
        "Cidade Atual: São Paulo\n"
        "Ações Restantes: 5\n"
        "Curas Descobertas: 1/5\n\n"
        "Status das Doenças:\n"
        "  • Vermelha: Nível 3\n"
        "  • Azul: Nível 1\n"
        "  • Amarela: Nível 0\n"
        "  • Verde: Nível 2\n"
        "  • Violeta: Nível 0\n\n"
        "Cartas na Mão:\n"
        "  • São Paulo (Vermelha)\n"
        "  • Rio de Janeiro (Azul)\n"
        "  • Evento: Bloquear Infecção\n"
    )

    while True:
        stdscr.clear()
        altura, largura = stdscr.getmaxyx()

        # Obtém o menu atual (topo da pilha)
        current_menu = menu_stack[-1]

        # Monta o texto do menu inferior dinamicamente
        menu_text = ""
        n = len(current_menu)
        # Exibe opções numeradas de 1 até n-1
        for i, opção in enumerate(current_menu[:-1]):
            menu_text += f"{i+1}. {opção}\n"
        # Exibe a opção 0 (última)
        menu_text += f"0. {current_menu[-1]}"

        # Usa a função de layout para desenhar as três áreas:
        #   - texto_central: área principal (acima)
        #   - menu_text: rodapé (menu interativo)
        #   - texto_lateral: parte direita (informações úteis)
        dividir_tela_em_tres(stdscr, texto_central, menu_text, texto_lateral)

        # Espera pela tecla do usuário
        ch = stdscr.getch()

        # Se for tecla '0'
        if ch == ord('0'):
            # Se estamos no menu principal e escolher "Sair" (última opção), encerra
            if len(menu_stack) == 1:
                break
            # Caso seja submenu, volta ao menu anterior
            else:
                menu_stack.pop()
                continue

        # Se for tecla entre '1' e '9'
        if ord('1') <= ch <= ord('9'):
            idx = ch - ord('1')
            # Verifica se a seleção está dentro do número de opções disponíveis (excluindo o "0")
            if idx < len(current_menu) - 1:
                escolha = current_menu[idx]
                # Se a opção escolhida tiver submenu definido, empilha esse submenu
                if escolha in menu_hierarchy:
                    menu_stack.append(menu_hierarchy[escolha])
                else:
                    # Para todas as opções sem submenu (mock-up), não faz nada além de exibir mensagem temporária
                    msg = f"Opção selecionada: {escolha}"
                    # Exibe mensagem de feedback por 1 segundo
                    stdscr.addstr(altura - 3, 2, msg)
                    stdscr.refresh()
                    curses.napms(1000)
                continue

        # Caso qualquer outra tecla seja pressionada, simplesmente continua o loop
        # (ignora teclas inválidas)
        continue

if __name__ == "__main__":
    curses.wrapper(main)
