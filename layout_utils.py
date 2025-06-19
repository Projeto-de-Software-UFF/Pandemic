import curses
import textwrap

def dividir_tela_em_tres(tela, texto_centro, texto_rodape, texto_lateral):
    tela.clear()

    altura, largura = tela.getmaxyx()
    divisor_vertical = (largura // 2) + 25
    divisor_horizontal = (altura // 2) + 6

    def exibir_texto_formatado(inicio_y, inicio_x, largura_max, altura_max, texto):
        linhas_quebradas = textwrap.wrap(texto, largura_max)
        for i, linha in enumerate(linhas_quebradas[:altura_max]):
            tela.addstr(inicio_y + i, inicio_x, linha)

    # Exibe conteúdo nas três áreas
    exibir_texto_formatado(1, 1, divisor_vertical - 2, divisor_horizontal - 2, texto_centro)
    exibir_texto_formatado(divisor_horizontal + 1, 1, divisor_vertical - 2, altura - divisor_horizontal - 2, texto_rodape)
    exibir_texto_formatado(1, divisor_vertical + 2, largura - divisor_vertical - 4, altura - 2, texto_lateral)

    # Desenha linhas divisórias
    for y in range(altura):
        tela.addch(y, divisor_vertical, '|')
    for x in range(divisor_vertical):
        tela.addch(divisor_horizontal, x, '-')

    tela.refresh()
