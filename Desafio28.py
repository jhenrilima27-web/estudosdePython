# Desafio 28
import random
from time import sleep
print ('\033[34m-=-\033[m'*17)
print ('\033[35;1m Vou pensar em um número entre 0 e 5. Tente adivinhar' )
print ('\033[34m-=-\033[35m'*17)
numa = int(input('Em qual número eu pensei ? '))
print ('\033[34m-=-\033[m'*17)
cert = random.randint(0,5)
print('\033[35;1m PROCESSANDO...')
sleep(2)
if numa == cert:
  print ('\033[32m PARABÉNS VC ACERTOU !!!!!')
else:
  print ('\033[31m Errouuuuuu pensei no número {} !!!'.format(cert))
