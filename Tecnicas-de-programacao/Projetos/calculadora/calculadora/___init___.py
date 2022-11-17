from funcoes import soma
from funcoes import subtracao
from funcoes import multiplicacao
from funcoes import divisao

def calcule(a,b,operacao):

    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação: ')

    if operacao == 'soma' or operacao == '+':
        return soma(a,b)
    elif operacao == 'subtracao' or operacao == '-':
        return subtracao(a,b)
    elif operacao == 'multiplicacao' or operacao == '*':
        return multiplicacao(a,b)
    else:
        return divisao(a,b)