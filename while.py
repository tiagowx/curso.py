# > LAÇO DE REPETIÇÃO "WHILE"

numero_sorteado = 15

numero_escolhido = int(input("Informe um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
  print("Você errou, tente novamente!")
  numero_escolhido = int(input("Informe um número entre 1 e 20: "))
  
print("Você acertou, parabéns!")

# COM CONTADOR

contador = 0

while(contador < 10):
  print(contador)
  contador += 1