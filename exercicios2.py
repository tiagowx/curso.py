# # # EXERCICIOS II # # #

#  QUESTÃO 1

# x = int(input("Digite um número inteiro: "))

# if x < 0 :
#     resp1 = "negativo"
# else:
#     resp1 = "positivo"
    
# if (x % 2) == 0 :
#     resp2 = "par"
# else:
#     resp2 = "impar"
    
# print("O número {0} é {1} e {2}.".format(x, resp1, resp2))


#  QUESTÃO 2

# cont = 0
# resultado = 0
# n = 1000

# while cont != n:

#     resultado = resultado + 1/(2**cont)
#     cont = cont + 1

#     if cont < 4:
#       print("{0} , {1}".format(cont, resultado))

# print(resultado)


#  QUESTÃO 3

# for _ in "let's code":
#   print("Olá, mundo!")

# for _ in " "*10:
#     print("Olá, mundo!")

# for _ in range(10, 20, 1):
#     print("Olá, mundo!")

# for _ in [10]: #**
#     print("Olá, mundo!")

# for _ in [10]*10:
#     print("Olá, mundo!")


# #  QUESTÃO 4

# lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

# lista_final = []

# for item in lista_inicial:

#     if item % 2 == 0:

#         if item < 0:

#             lista_final.append(-item)
    
#         else:

#             lista_final.append(item)
#     else:

#         if item < 0:
            
#             lista_final.append(-item*2)
    
#         else:

#             lista_final.append(item*2)
            
# print(lista_final)


#  QUESTÃO 4

animais = ['gato', 'coelho', 'macaco', 'girafa']

animais.remove('gato')
print(animais)
print(len(animais))
print(animais.index('coelho'))