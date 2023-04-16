# > DICIONÁRIOS

# Como criar um 'dicionário'
dicionario = {}
dicionario = dict()

dicionario = {"nome": "Tiago", "idade": 30, "altura": 1.89}

print(dicionario)
print(dicionario["idade"])


# Adicionando elementos a um 'dicinário'
dicionario["programador"] = True
print(dicionario)

# Mudar valor de um elementos a um 'dicinário'
dicionario["altura"] = 3
print(dicionario)

# Iterando sobre 'dicionário'
for chave in dicionario:
  print(chave, dicionario[chave])
  
# Testar se chave já existe
print("peso" in dicionario)
print("altura" in dicionario)