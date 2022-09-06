def adic(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def di(x, y):
  return x/ y

print('Selecione o número da operação desejada: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Todas')

escolha = int(input('\nDigite sua opção (1/2/3/4/5): '))
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if escolha == 1:
  print()
  print(f'{n1} + {n2} = {adic(n1,n2)}')
  print()
elif escolha == 2:
  print()
  print(f'{n1} - {n2} = {sub(n1,n2)}')
  print()
elif escolha == 3:
  print()
  print(f'{n1} x {n2} = {mult(n1,n2)}')
  print()
elif escolha == 4:
  print()
  print(f'{n1} / {n2} = {di(n1,n2)}')
  print()
elif escolha == 5 :
  print(f'{n1} + {n2} = {adic(n1,n2)}')
  print(f'{n1} - {n2} = {sub(n1,n2)}')
  print(f'{n1} * {n2} = {mult(n1,n2)}')
  print(f'{n1} / {n2} = {di(n1,n2)}')
else:
  print('Opção inválida....')