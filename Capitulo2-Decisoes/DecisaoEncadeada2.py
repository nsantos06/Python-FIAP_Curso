nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()

#Primeiro problema a ser resolvido

if doenca_infectocontagiosa == "SIM":
    print("Encaminhe o paciente para sala Amarela.")
elif doenca_infectocontagiosa == "NAO":
    print("Encaminhe o paciente para sala Branca.")
else:
    print("Responda a pergunta com SIM ou NAO")

#Segundo problema a ser resolvido

if idade >= 65:
    print("Paciente com prioridade")
else:
    genero = input("Digite o genero do paciente").upper()
    if genero == "Feminino" and idade >10:
        gravidez = input("A paciente esta grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente com Prioridade")
        else:
            print("Paciente sem Prioridade")
    else:
        print("Paciente sem Prioridade")

