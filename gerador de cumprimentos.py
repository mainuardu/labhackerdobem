from random import *

executa = True

adjetivos = ["maravilhoso", "acima da média", "excelente", "lindo", "incrível"]
hobbies = ["andar de bicicleta", "programar", "jogar bola", "jogar videogame"]

print("Gerador de Cumprimentos")
print("-----------------------")

print("Qual o seu nome?")
nome = input()

print(nome+''' escolha uma das opções:
c - obter cumprimento
q - sair
''')

while executa == True:
  opcao = input().lower()
  if opcao == 'c':
    print("Aqui está o seu cumprimento",nome,":")
    print(nome,"você é",choice(adjetivos),"em",choice(hobbies))
    print("De nada")
  elif opcao == 'q':
    executa = False
  else:
    print("Escolha um opção válida!")
