# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
from ex111 import moedas
from ex111 import dados
test = dados.leiaDinheiro('Digite o preço: R$')
moedas.resumo(test, 10, 10)
