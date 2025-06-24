🦠 MicroPandemic
Um mini-jogo de terminal inspirado em Pandemic, focado em ações táticas contra surtos de doenças. Este projeto simula as interações principais de um turno de jogador com base em menus, usando uma interface em terminal com curses.

🎮 Funcionalidades
Interface de terminal dividida em três áreas:

Centro: Mensagens de status e introdução.

Rodapé: Menu de ações disponíveis.

Lateral: Informações do jogador e do jogo.

Navegação interativa por menus com teclas numéricas.

Estrutura modular e extensível para adição de lógica de jogo real.

💻 Tecnologias
Python 3.7+

Biblioteca curses (já embutida no Python para Linux/macOS)

▶️ Como executar
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seuusuario/micropandemic.git
cd micropandemic
Execute o jogo:

bash
Copiar
Editar
python main.py
⚠️ No Windows, é recomendável usar WSL (Windows Subsystem for Linux) para compatibilidade com curses.

🧱 Estrutura do Projeto
bash
Copiar
Editar
micropandemic/
├── main.py                 # Loop principal e controle de menu
├── layout_utils.py         # Função de layout da interface (tela dividida)
├── README.md               # Este arquivo
├── requirements.txt        # (Opcional) dependências futuras
📋 Controles
Use números 1 a 9 para navegar entre opções.

Pressione 0 para retornar ao menu anterior ou sair do jogo.

📌 Planejamento Futuro
Integração com regras reais de Pandemic.

Representação gráfica de cidades e conexões.

Inventário de cartas real.

Sistema de multiplayer local.

📝 Licença
MIT © 2025 — Projeto educacional de Engenharia de Software.
