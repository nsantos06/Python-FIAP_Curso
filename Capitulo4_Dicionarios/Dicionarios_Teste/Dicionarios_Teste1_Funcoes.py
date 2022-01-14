def inserirAdmin(dicionario_admin):
    dicionario_admin[int(input("Digite o ID do admin:"))] = [input("Digite o nome do admin:"),
                                                    input("Digite a area:"),
                                                    input("Digite o cargo:")
                                                    ]
def inserirFuncionario(dicionario_funcionario):
    dicionario_funcionario[int(input("Digite o ID do funcionário:"))] = [input("Digite o nome do funcionario:"),
                                                          input("Digite a área a qual o funcionario trabalhe:"),
                                                          input("Digite o cargo do funcionário:")
                                                          ]

def cadastrarPessoas(dicionario_pessoas):
    opcao = input("Digite a opção: \n"
                  "<F> para funcionários \n"
                  "<A> para ADM \n"
                  "para cadastro:").upper()

    while opcao == "A" or opcao == "F":
        if opcao == "A":
            inserirAdmin(dicionario_pessoas)
        elif opcao == "F":
            inserirFuncionario(dicionario_pessoas)
        else:
            print("Digite <F> ou <A>, para cadastrar.")
        opcao = input("Quem deseja cadastrar?").upper()
