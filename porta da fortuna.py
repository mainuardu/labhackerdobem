from random import *

#imprima as 3 portas e as intruçoes do jogo
print('''
porta da fortuna!
=========

existe um super premio atras de uma destas 3 portas!
adivinhe qual e a porta certa para ganhar o premio

  _____    _____    _____
 |     |  |     |  |     |
 | (1) |  | (2) |  | (3) |
 |    o|  |    o|  |    o|
 |_____|  |_____|  |_____|

 escolha uma porta (1, 2, ou 3)
 ''')

#pegue a porta escolhida e a armazene como um numero inteiro (int)
portaescolhida = input()
portaescolhida = int(portaescolhida)

#escolha aleatoriamente a porta que esconde o premio (entre 1 e 3)
portacerta = randint(1,3)

#mostre ao jogador qual porta ele escolheu e qual era a certa
print("a porta escolhida fia", portaescolhida)
print("a porta certa e a", portacerta)

#o jogador ganha se o numero da porta escolhida e da certa forem o mesmo
if portaescolhida == portacerta:
    print("parabens")
else:
    print("que pena")
 
