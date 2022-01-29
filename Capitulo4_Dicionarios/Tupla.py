ips = {}
resp = "S"
while resp == "S":
    ips[(input("Digite os primeiros octetos: "),
        input("Digite os ultimos octetos: "))] = input("Nome da máquina: ")

    resp = input("Digite <S> para continuar: ").upper()

print("Exibindo ips: ")
for ip in ips.keys():
    print(ip[0] + " " + ip[1])

print("Exibindo máquinas com o mesmo endereço:")
pesquisa = input("Digite os dois ultimos octetos:")
for ip, nome in ips.items():
    print("Maquinas no mesmo endereço (redes diferentes)")
    if (ip[1] == pesquisa):
        print("nome")

print("Exibindo as máquinas com a mesma rede:")
rede = input("Digite o nome das redes:")
for ip, nome in ips.items():
    print("Maquinas no mesmo endereço (redes diferentes)")
    if (ip[0] == rede):
        print("nome")
