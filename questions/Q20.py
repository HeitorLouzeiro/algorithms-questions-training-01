'''
Faça um programa que receba a medida do ângulo formado
por uma escada apoiada no chão e a distância em que a escada está da parede,
calcule e mostre a medida da escada para que se possa alcançar sua ponta.
'''
import math

angle = 5  # angulo
distance = 3  # altura da escada

'''
Convertendo o angulo para radianos unidade
de medidas da função trigonometrica.
'''
height = distance * math.tan(math.radians(angle))
'''
tan é a tangente do angulo ou seja lado oposto
comprimento do lado oposto (altura).
multiplicando a com a distacia obtemos a altura para alcançar a parede.
'''
# usa Teorema de Pitágoras para calcular a distancia da escada.
# raiz(hipotenusa) = cateto1**2 + cateto2**2
stairMeasurement = math.sqrt(height ** 2 + height ** 2)

print("Stair Measurement is {:.2f} metros.".format(stairMeasurement))
