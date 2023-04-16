# LAÇOS DE REPETIÇÃO COM 'FOR"

# for i in range(10):
#   print(i)

# for i in range(1, 10):
#   print(i)

# for i in range(1, 12, 3):
#   print(i)

soma = 0

for i in range(3):
  nota = float(input(f"Informa sua nota {i + 1}: "))
  
  soma += nota
  
  
print(f"Sua média é: {soma / 3}")