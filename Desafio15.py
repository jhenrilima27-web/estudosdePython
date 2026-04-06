dia = int(input('Quantos dias o carro ficou alugado ? '))
km = float(input('Quantos km rodados ? '))
valor = dia*60 + km*0.15
print ('O valor a pagar é R${:.2f}'.format(valor))
