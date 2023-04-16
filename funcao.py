# > FUNÇÕES

# Funções já utilizadas
# print() # Exibe uma saida no teminal
# input() # Solicita uma entrada o usuário
# len()   # Quantifica os elementos de uma lista
# max()   # Retorna o elemento de valor mais alto dentro de uma lista

# Criando uma 'função'

# def saudacao():
#   print("Seja bem vindo(a)")
  
# saudacao()

# Criando uma 'função' com parâmetro

# def saudacao(nome, curso):
#   print(f"Seja bem vindo(a) {nome} ao curso de {curso}!")
  
# saudacao('Tiago', 'Python')

# Criando uma 'função' com parâmetro 'default'

# def saudacao(nome, curso='Python'):
#   print(f"Seja bem vindo(a) {nome} ao curso de {curso}!")
  
# saudacao('Tiago')
# saudacao('Tiago', "C++")


# Criando uma 'função' com rretorno
# def soma(num1, num2):
#   return num1+num2 

# print(soma(20,12))

# Calculadora

def calculadora (n1, n2, op = "+"):
  if(op == "+"):
    return n1 + n2
  elif (op == "-"):
    return n1 - n2
  elif (op == "*"):
    return n1 * n2
  elif (op == "/"):
    return n1 / n2
  
print(calculadora(3,4))
print(calculadora(3,4,"-"))
print(calculadora(3,4,"*"))
print(calculadora(3,4,"/"))