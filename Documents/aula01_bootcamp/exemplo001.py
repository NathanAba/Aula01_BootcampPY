# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu.

a = input("Olá! Qual o seu nome? ")

b = float(input(a +", Qual o seu salário Mensal? "))

c = float(input(a + ", Qual a porcentagem de aumento teve esse ano? "))

d = b * (c /100) #Valor do aumento

novo_salario = b + d

print("Certo, " + a + "! Seu salário é de R$ " + str(b) +
      " e você teve um bônus de " + str(c) + "%." +
      " Com isso, você teve um aumento de R$ " + str(d) +
      " e seu salário ficou em R$ " + str(novo_salario) + ".")