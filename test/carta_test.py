
import pytest
from domain.carta.carta import Carta, TipoCarta
from domain.carta.eventodoenca import EventoDoenca
from domain.carta.construircentropesquisa import Construircentropesquisa

# Teste básico para a classe Carta com tipo CIDADE
def test_carta_cidade_repr():
    carta = Carta(nome="São Paulo", tipo=TipoCarta.CIDADE)
    assert repr(carta) == "Cidade: São Paulo"

# Teste básico para a classe Carta com tipo EVENTO
def test_carta_evento_repr():
    carta = Carta(nome="Airlift", tipo=TipoCarta.EVENTO)
    assert repr(carta) == "Evento: Airlift"

# Teste para verificar se Eventodoenca guarda a cor corretamente
def test_evento_doenca_tem_cor():
    evento = EventoDoenca(cor="vermelho")
    assert evento.cor == "vermelho"

# Teste para verificar se Construircentropesquisa guarda o nome corretamente
def test_construir_centro_pesquisa_nome():
    centro = Construircentropesquisa("Paris")
    assert centro.nome == "Paris"
    
# Teste para garantir que Construircentropesquisa é uma subclasse de Carta e tem tipo correto
def test_construircentropesquisa_herda_carta():
    carta = Construircentropesquisa("Atlanta")
    assert isinstance(carta, Carta)
    assert carta.tipo == TipoCarta.CIDADE

# Teste para garantir que Eventodoenca é uma subclasse de Carta e tem tipo correto
def test_eventodoenca_herda_carta():
    carta = EventoDoenca("azul")
    assert isinstance(carta, Carta)
    # Pode ser TipoCarta.EPIDEMIA ou TipoCarta.EVENTO dependendo da sua definição
    assert carta.tipo == TipoCarta.EPIDEMIA or carta.tipo == TipoCarta.EVENTO
