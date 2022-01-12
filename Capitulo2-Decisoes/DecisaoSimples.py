paciente = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
prioridade = "NAO"
if idade >= 65:
    prioridade = "SIM"
print("O paciente " + paciente + " possui atendimento prioritário? " + prioridade)
