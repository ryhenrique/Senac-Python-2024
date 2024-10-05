#Para o lar:  Faça um programa que diga se um número é divisivel por 3 e que diga se um numero é divisivel por 5

print("Seja bem-vindo(a) ao cálculo de divisor por 3 e 5!")
numero = int(input("Digite o seu número:"))

if (numero % 3 == 0):
    print(f"O seu número: {numero} é divisível por 3!")
elif (numero % 5 == 0):
    print(f"O seu número: {numero} é divisível por 5!")
else:
    print(f"O seu número: {numero} não é divisível por 3")
    print(f"O seu número: {numero} não é divisível por 5")