from abc import ABC, abstractmethod
from typing import List

class Operacao(ABC):
    operador: float

    def __init__(self, n):
        self.operador = n

    @abstractmethod
    def calcular(self, n: float):
        pass

    @abstractmethod
    def calcular_inverso(self, n: float):
        pass

class Adicao(Operacao):
    def calcular(self, n: float):
        return n + self.operador

    def calcular_inverso(self, n: float):
        return n - self.operador
class Subtracao(Operacao):
    def calcular(self, n: float):
        return n - self.operador

    def calcular_inverso(self, n: float):
        return n + self.operador

class Multiplicacao(Operacao):
    def calcular(self, n: float):
        return n * self.operador

    def calcular_inverso(self, n: float):
        return n / self.operador

class Divisao(Operacao):
    def calcular(self, n: float):
        return n / self.operador

    def calcular_inverso(self, n: float):
        return n * self.operador

class Calculadora:
    resultado: float
    operacoes: List[Operacao]

    def __init__(self):
        self.resultado = 0
        self.operacoes = []

    def add_operacao(self, op : Operacao):
        self.operacoes.append(op)

    def calcular_total(self):
        calculo = 0
        for op in self.operacoes:
            calculo = op.calcular(calculo)
        self.resultado = calculo

    def desfazer_ultima(self):
        op = self.operacoes.pop()
        self.resultado = op.calcular_inverso(self.resultado)

if __name__ == "__main__":
    a1 = Adicao(4)
    s1 = Subtracao(2)
    m1 = Multiplicacao(4)
    d1 = Divisao(2)
    calc = Calculadora()
    calc.add_operacao(a1)
    calc.add_operacao(s1)
    calc.add_operacao(m1)
    calc.add_operacao(d1)
    calc.calcular_total()
    print(calc.resultado)
    calc.desfazer_ultima()
    print(calc.resultado)


