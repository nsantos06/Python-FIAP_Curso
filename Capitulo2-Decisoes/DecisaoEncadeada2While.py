resposta = "SIM"

while resposta == "SIM":
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()

    #Primeiro problema a ser resolvido
    while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
        print("Digite SIM ou NAO")
        doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa?").upper()

    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe o paciente para sala Amarela.")
    else:
        print("Encaminhe o paciente para sala Branca.")

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

    resposta = input("Digite SIM para continuar!").upper()
