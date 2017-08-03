'''
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:
Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
Exemplos:
Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
'''
def sacar(valor):
    notas = (100,50,20,10)
    saque = []
    for nota in notas:
        while valor >= nota:
            saque.append(nota)
            valor -= nota
        if valor == 0:
            break

    return saque


assert sacar(10) == [10]
assert sacar(20) == [20]
assert sacar(50) == [50]
assert sacar(100) == [100]

assert sacar(30) == [20,10]
assert sacar(40) == [20,20]
assert sacar(60) == [50,10]

assert sacar(80) == [50,20,10]
assert sacar(200) == [100,100]