#listas vazias
equipamentos = []
valores = []
numero_serial = []
departamentos = []

#adicionando elementos às listas
resposta = "SIM"
while resposta == "SIM":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    numero_serial.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento: "))

    resposta = input("Digite SIM para continuar: ").upper()

#imprimindo os equipamentos
for indice in range(0, len(equipamentos)):
    print("\nEquipamento:..: ", (indice + 1))
    print("Nome...", equipamentos[indice])
    print("Valor...", valores[indice])
    print("Serial...", numero_serial[indice])
    print("Departamento...", departamentos[indice])


#buscar equipamentos

resposta_busca = input("Deseja realizar uma busca? Digite SIM: ").upper()
while resposta_busca == "SIM":
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for indice in range(0, len(equipamentos)):
        if busca == equipamentos[indice]:
            print("\nValor...:", valores[indice])
            print("Serial...:", numero_serial[indice])
        if busca != equipamentos[indice]:
            resposta_busca = input("Caso queira buscar novamente, digite SIM ").upper()

#excluindo um numero serial
serial = int(input("Digite o numero serial do item a ser excluido: "))
for indice in range(0, len(departamentos)):
    if numero_serial[indice] == serial:
        del departamentos[indice]
        del equipamentos[indice]
        del numero_serial[indice]
        del valores[indice]
        break
