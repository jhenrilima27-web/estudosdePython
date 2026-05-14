# Desafio 29
vel = int(input('Qual a velocidade do carro ? '))
if vel>80:
  print('MULTADO! Você excedeu o limite de  velocidade que é 80km/h')
  print('Valor da multa: R${},00 reais '.format((vel-80)*7))
else:
  print('Tenha um bom dia ! Dirija com segurança!')
