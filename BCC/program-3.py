# Faça um programa que lê um número inteiro 𝑛 e imprime a mensagem:
# “O numero eh par” (caso 𝑛 seja par)
# “O numero eh impar” (caso 𝑛 seja ímpar)

# Dados de inout chegam como string portanto é necessário fazer um cast do tipo 
dadoDeEntrada = int(input("Por favor digite um número " ))


if dadoDeEntrada%2 == 0:
  print("Esse é um número par!")
else:
  print("Esse número é ímpar!")


