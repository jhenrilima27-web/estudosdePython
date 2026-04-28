num = int(input('inform a number'))
uni = num//1 % 10
des = num//10 % 10
cen = num//100 % 10
mil = num//1000 % 10
print ('Analizando o número {}'.format(num))
print ('Unidade: {}'.format(uni))
print ('Dezena: {}'.format(des))
print ('Centena: {}'.format(cen))
print ('Milhar: {}'.format(mil))
