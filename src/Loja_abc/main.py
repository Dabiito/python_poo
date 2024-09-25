from common import *

if __name__ == '__main__':
    g = Gerente("rogerio", "12354", 1234)
    print(g)
    if g.autenticar("12354", 1234):
        print(g.cancelarOperacao())
    else:
        print("Falha na autentificacao")

    op = OperadorCaixa("Ronaldo", "1245", 4445, 8889)
    print(op)
    if op.autenticar("8889", 4445):
        print(op.registrar_produto())
    else:
        print("Falha na autentificacao")

    seg = Seguranca("Rog", "1234", 1235, 32)
    print(seg)
    if seg.autenticar("32", 1235):
        print(seg.acionarAlarme())
    else:
        print("Falha na autentificacao")