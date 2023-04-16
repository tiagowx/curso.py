# ESTRUTURA DE "LISTAS"

## Antes
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

## Com lista
nota = [7.9, 9.7, 8.2]

# Criando listas

lista = []
lista = list()
lista = [26, "Tiago", 1.468, False]
lista_de_listas = [26, ["Tiago", 1.468, True]]

# print(lista)
print(lista)
print(lista_de_listas)

# Idexação
lista = [26, "Tiago", 1.468, False]

print(lista[3])
print(lista[1])
print(lista[0])
print(lista[2])

print(lista[-2]) # imprime na ordem inversa 

# Slices
lista = [10,20,30,40,50,60,70]
print(lista[0:3])
print(lista[2:5])
print(lista[2:])
print(lista[1:6:2])
print(lista[1::2])


# Interando com o 'for'
for elemento in lista:
  print(elemento)
  
print('Comprimento da lista é: ', len(lista))


for i in range(len(lista)):
  print(lista[i])
  
# MÉTODOS DE LISTAS

lista = [1,3,12,8,2]

# 'append'
print ("Antes do 'append': ", lista)

lista.append(4)

print ("Depois do 'append': ", lista)

# 'insert'
lista.insert(2,10)

print ("Depois do 'insert':", lista)

# 'extend'
lista2 = [5,8,13,2,12]
lista.extend(lista2)

print ("Depois do 'extend':", lista)

# 'pop'
lista.pop()
print ("Depois do 'pop':", lista)

# 'pop' com parametro
lista.pop(2)
print ("Depois do 'pop(2)':", lista)

# 'remove'
lista.remove(8)
print ("Depois do 'remove':", lista)

# 'count'
print ("Quantidade de elementos '2': ", lista.count(2))

# 'index'
print ("Index do elemento '12': ", lista.index(12))

# 'sort'
lista.sort()
print ("Lista ordenada por 'sort' : ", lista)

# 'sort' parametro 'reverse = true'
lista.sort(reverse = True)
print ("Lista ordenada por 'sort' : ", lista)


# FUNÇÕES DE LISTAS 

# len ()
print( "quantidade de elementos na lista é: ", len(lista))

# sum ()
print( "quantidade de elementos na lista é: ", sum(lista))

# max ()
print( "o maior valor  na lista é: ", max(lista))

# min ()
print( "o menor valor na lista é: ", min(lista))

