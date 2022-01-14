def perguntar():
    return input("O que deseja fazer?\n"
              "<I> para inserir usuário\n"
              "<P> para pesquisar usuário\n"
              "<E> para excluir usuário\n"
              "<L> para listar os usuários\n"
              "<S> para sair.\n").upper()

def inserir(dicionario):
    dicionario[input("Digite o nome:").upper()] = [input("Digite o login:").upper(),
                                                 input("Digite a data:"),
                                                 input("Digite a ultima estação a ser acessada:").upper()
                                                 ]
#pesquisar em qual dicionario, e a chave(o que, dentro dessa chave, será pesquisado.)
#Verificamos se a lista está vazia ou não, caso esteja com um elemento, ou cheia,
#exibiremos os dados que compõem a lista. Caso não encontre a chave, não retornará nada.

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome...:", lista[0])
        print("Ultimo acesso...:", lista[1])
        print("Ultima estacao...:", lista[2])

#qual dicionario será excluido, e qual dado dele (chave) será excluida
def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto eliminado:")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto..:")
        print("Login: ", chave)
        print("Dados: ", valor)
