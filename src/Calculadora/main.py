from Calculadora import *
from typing import Type

if __name__ == "__main__":
    print("Calculadora Iniciada!")
    print("Digite '=' para calcular o total.")
    print("Digite 'd' para desfazer a última operação.")
    print("Digite 'q' para sair.")

    calc = Calculadora()
    print(f'>> {calc.resultado}')
    op = input('>> ')

    while op != 'q':
        if op == '+' or op == '-' or op == '*' or op == '/':
            n = float(input('>> '))

            if op == '+':
                o = Adicao(n)
            elif op == '-':
                o = Subtracao(n)
            elif op == '*':
                o = Multiplicacao(n)
            elif op == '/':
                o = Divisao(n)

            calc.add_operacao(o)

        elif op == '=':
            calc.calcular_total()
            print(f'>> {calc.resultado}')

        elif op == 'd':
            calc.desfazer_ultima()
            print(f'>> {calc.resultado}')

        else:
            print('>> Não entendi')

        op = input('>> ')
