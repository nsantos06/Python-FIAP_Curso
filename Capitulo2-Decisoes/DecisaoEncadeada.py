nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()

if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe para sala amarela.")
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe para sala branca.")
    else:
        print("Responda a pergunta com SIM ou NAO")
else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe para sala amarela.")
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe para sala branca.")
    else:
        print("Responda a pergunta com SIM ou NAO")

