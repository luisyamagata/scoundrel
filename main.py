import regras
import pygame

print('Bem-Vindo ao Scoundrel')
menu = int(input(''' Digite:
      [0] Para ler as regras
      [1] Para jogar
      [2] Para sair
'''))
#print(menu)
if menu == 0:
    regras.regras()