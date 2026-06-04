peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print("Seu IMC é:", round(imc, 2))

if imc < 18.5:
    print("Você está abaixo do peso")

elif imc < 25:
    print("Você está com peso normal")

elif imc < 30:
    print("Você está com sobrepeso")

else:
    print("Você está com obesidade")
