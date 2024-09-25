from abc import ABC, abstractmethod

class Funcionario(ABC):
    nome: str
    cpf: str
    __senha: int

    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.__senha = senha

    @abstractmethod
    def autenticar(self, user: str, senha: int):
        pass

    def get_senha(self):
        return self.__senha

    def __str__(self):
        info = f'Nome: {self.nome}\n'
        info += f'Cpf: {self.cpf}'
        return info

class Gerente(Funcionario):

    def autenticar(self, user: str, senha: int):
        if user == self.cpf and senha == self.get_senha():
            return True
        else:
            return False

    def cancelarOperacao(self):
        info = f'Cancelando Operacoes'
        return info

class OperadorCaixa(Funcionario):
    numeroCaixa: int

    def __init__(self, nome, cpf, senha, numeroCaixa):
        super().__init__(nome, cpf, senha)
        self.numeroCaixa = numeroCaixa

    def autenticar(self, user: str, senha: int):
        if user == str(self.numeroCaixa) and senha == self.get_senha():
            return True
        else:
            return False

    def registrar_produto(self):
        info = f'Produto registrado com Sucesso'
        return info

class Seguranca(Funcionario):
    posto: str

    def __init__(self, nome, cpf, senha, posto):
        super().__init__(nome, cpf, senha)
        self.posto = posto

    def autenticar(self, user: str, senha: int):
        if user == str(self.posto) and senha == self.get_senha():
            return True
        else:
            return False

    def acionarAlarme(self):
        info = f'Uooooooooouuuuooooouuuoouuuu!'
        return info