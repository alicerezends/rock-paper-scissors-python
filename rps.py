import random

opcoes = ["pedra", "papel", "tesoura"]

computador = random.choice(opcoes)

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

print("Computador:", computador)
print("Jogador:", jogador)

if jogador == computador:
    print("Empate!")

elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("VOCÊ VENCEU!")

elif jogador in opcoes:
    print("Você perdeu!")

else:
    print("Opção inválida!")
