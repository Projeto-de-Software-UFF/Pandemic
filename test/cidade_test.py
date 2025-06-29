from domain.cidade import Cidade

c1 = Cidade('Rio de Janeiro')
c2 = Cidade('São Paulo')
c3 = Cidade('Baia')

c1.adicionarCidadeVizinha([c2])
c2.adicionarCidadeVizinha([c1, c3])
print(c2.vizinhacidade)
print(c2.centropesquisa_existe())
