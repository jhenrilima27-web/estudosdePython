largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = altura*largura
print ('Sua parede tem a dimensão de {}x{} e sua área é de {}m^2'.format(largura,altura,area))
print ('Para pintar essa parede, você precisará de {}l de Tinta'.format(area/2))
