import math
cateto1 = float(input('qual o valor do cateto oposto '))
cateto2 = float(input('Qual o valor do cateto adjacente '))
hip = (cateto1**2 + cateto2**2)**(1/2)
print ('A hipotenusa vale {}'.format(hip))