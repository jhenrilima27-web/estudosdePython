# Desafio 26
nomed = str(input('Qual o seu nome ? ')).strip().lower()
print ('a letra a apareceu {} vezes'.format(nomed.count('a')))
print ('A primeira letra a apareceu na {} posição'.format(nomed.find('a')+1))
print ('A ultima letra a apareceu na {} posição'.format(nomed.rfind('a')+1))
