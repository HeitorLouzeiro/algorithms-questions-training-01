'''
Faça um programa que receba o raio,
calcule e mostre:
a) o comprimento de uma esfera;
sabe-se que c = 2 * p R;
b) a área de uma esfera; sabe-se que A = p R2;
c) o volume de uma esfera;
sabe-se que v = ¾ * p R3.

'''
import math

ray = float(input('Enter the value of the radius:'))

sphereLenght = 2 * math.pi * ray
sphereArea = math.pi * ray**2
sphereVolume = (3/4) * math.pi * ray**3

print('Sphere lengt:{:.2f}'.format(sphereLenght))
print('Sphere Area:{:.2f}'.format(sphereArea))
print('Sphere Volume:{:.2f}'.format(sphereVolume))
