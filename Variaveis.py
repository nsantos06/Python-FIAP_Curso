nome = input("Digite um funcionario: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
mediaMensalidade = float(input("Digite a média de mensalidade: "))

print(nome + " Trabalha na empresa " + empresa)
print("Possui:", qtde_funcionarios, "funcionários.")
print("A média de mensalidade é de: " + str(mediaMensalidade))

print("==============Verifique os tipos de dados abaixo:==============")

print("O tipo de dado da variavel [nome] é: ", type(nome))
print("O tipo de dado da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variavel [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))
