nivel = input("Digite o seu nivel:").upper()
if nivel == "ADM" or "USR":
    genero = input("Digite o genero:").upper()
    if nivel == "ADM":
        if genero == "FEMININO":
            print("Olá Administradora!")
        else:
            print("Olá Administrador!")

    else:
        if genero == "FEMININO":
            print("Olá usuaria!")
        else:
            print("Olá usuario!")

elif nivel == "GST":
    print("Ola visitante!")
else:
    print("olá desconhecido(a)!")

