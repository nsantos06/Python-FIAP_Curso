numero = int(input("Digite um numero: "))
print("Numero da tabuada:", numero)
for valor in range(1,11,1):
    print(str(numero) + " x " + str(valor) + " = " + str(numero * valor))
