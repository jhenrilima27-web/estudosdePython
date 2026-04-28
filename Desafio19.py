import random
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('nome do segunndo aluno: ')
aluno3 = input('nome do terceiro aluno: ')
aluno4 = input('nome do quarto aluno: ')
lista = [aluno1,aluno2,aluno3,aluno4]
print ('O aluno escolhido foi o/a {}'.format(random.choice(lista)))
