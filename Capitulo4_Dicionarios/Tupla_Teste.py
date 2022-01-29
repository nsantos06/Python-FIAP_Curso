usuarios = {}
emails = []

resp = "S"
while resp == "S":
    emails.append(input("Digite os emails:").lower())
    resp = input("Digite <S> para continuar: ").upper()

tupla = list(enumerate(emails))
for chave in range(0, len(tupla)):
    print("Email:", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nivel:")]
