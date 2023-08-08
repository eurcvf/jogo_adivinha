# 1 - Importar as bíbliotecas
import random
import time
import os

# 2 - Separar o jogo de adivinha o número em funções

# Titulo ao iniciar o jogo
def titulo():
  print('\n' + ('@' * 38) + '\n')
  print('\t JOGO DO ADIVINHA')
  print('\n' + ('@' * 38) + '\n')
  
# Gerar números randomicos
def gerar_numeros_aleatorio():
  numero_gerado = random.randrange(1,101)
  return numero_gerado

# Função principal do jogo
def desafiador(numero, tentativa):
  while True:
    try:
      tentativa_numero = int(input('\nTente acertar o número que estou pensando de 1 a 100. \nR: '))
      if tentativa_numero > 100 or tentativa_numero < 1:
        time.sleep(1)
        print('\nInforme um número de 1 a 100!')
      elif tentativa_numero > numero:
        time.sleep(1)
        print(f'\nO número é menor que {tentativa_numero}!')
        tentativa += 1
        if tentativa == 1:
          print(f'Número de tentativas: {tentativa} vez')
        else:
          print(f'Número de tentativas: {tentativa} vezes')
        time.sleep(1)
      elif tentativa_numero < numero:
        time.sleep(1)
        print(f'\nO número é maior que {tentativa_numero}!')
        tentativa += 1
        if tentativa == 1:
          print(f'Número de tentativas: {tentativa} vez')
        else:
          print(f'Número de tentativas: {tentativa} vezes')
        time.sleep(1)
      elif tentativa_numero == numero:
        time.sleep(1)
        print(f'\nPARABÉNS! Você acertou o número gerado. \nNúmero Gerado: {numero} \nNúmero Chute: {tentativa_numero}')
        print(f'Foi preciso {tentativa} tentativas para acertar o número!')
        time.sleep(1)
        continuarJogando = input('\nVocê gostaria de continuar jogando? [S ou N]')
        if continuarJogando.upper() == 'S' or continuarJogando.upper() == 'SIM':
          time.sleep(1)
          print('\nOPS! Parece que há um hacker no sistema, o jogo está sendo reiniciado!!!')
          time.sleep(1)
          numero = gerar_numeros_aleatorio()
          tentativa = 0
          os.system('cls')
          titulo()
        elif continuarJogando.upper() == 'N' or continuarJogando.upper() == 'NAO' or continuarJogando.upper() == 'NÃO':
          print('\nÉ uma pena que não queira jogar novamente, até mais!')
          os.system('cls')
          break
    except ValueError:
      print('Informe somente números inteiros!')
      time.sleep(1)

titulo()
input('Pressione [ENTER] para iniciar a jogatina!')
numero = gerar_numeros_aleatorio()
tentativa = 0
desafiador(numero,tentativa)

  