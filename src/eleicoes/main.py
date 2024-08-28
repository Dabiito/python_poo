import pickle
import traceback

from common import *

FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'


def menu_candidato():
    print("1-Novo Candidato")
    print("2- Listar Candidatos")
    print("3- Sair")
    op = int(input("DIgite a opcao [1,2,3]? "))
    while op not in (1,2,3):
        op = omt(input("Digite a opcap [1,2,3]? "))
    return op

def inserir_candidatos(candidatos):
    numero = int(input("Digite o numero do candidato: "))

    if numero in candidatos:
        raise Exception("Candidato já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[numero] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print('Candidato gravado com sucesso!')
    print(candidato)

def lista_candidatos(candidatos):
    for c in candidatos.values():
        print(c)
def menu_eleitor():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def inserir_eleitor(eleitores):
    titulo = int(input("Digite o Títlulo: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = input("Digite a secao: ")
    zona = input("Digite a zona: ")

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def atualizar_eleitor(eleitores):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = input("Digite a nova secao: ")
        zona = input("Digite a nova zona: ")
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')

if __name__ == "__main__":
    eleitores = {} #dicionário a chave será o titulo
    candidatos = {}
    try:
        print("Carregando arquivo de eleitores ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)

            print("Carregando arquivo de candidatos ...")

            with open(FILE_CANDIDATOS, 'rb') as arquivo:
                candidatos = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado!")


    op_usr = 1
    while op_usr in (1,2):
        op_user = int(input("Gerenciar: 1- Candidatos 2- Eleitores [1,2]: "))

        if op_usr == 1:
            opcao = 1
            while opcao in (1,2,3):
                try:
                    opcao = menu_candidato()

                    if opcao == 1:
                        inserir_candidatos(candidatos)
                    elif opcao == 2:
                        lista_candidatos(candidatos)
                    elif opcao == 3:
                        print('Saindo...')
                        break
                except Exception as e:
                    print("Erro")
    else:
        opcao = 1
        while opcao in (1,2,3):
            try:
                opcao = menu_eleitor()

                if opcao == 1:
                    inserir_eleitor(eleitores)
                elif opcao == 2:
                    atualizar_eleitor(eleitores)
                elif opcao == 3:
                    print("Saindo!")
                    break
            except Exception as e:
                #traceback.print_exc()
                print(e)