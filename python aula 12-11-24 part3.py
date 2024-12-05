idades = []

while True:
    idade = int(input("Digite uma idade ou 0 para sair:"))
    if idade == 0:
        break
idades.append(idade)

media = sum(idade) /len(idades)
soma= sum(idades)
tamanho= len(idades)

print(f"A soma das idades é: {soma}")
print(f"A média das idades é: {media}")
print(f"Foi inserido {tamanho} idades.")