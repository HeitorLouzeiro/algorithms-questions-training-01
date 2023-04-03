'''
Faça um programa que receba o valor dos catetos de um triângulo,
calcule e mostre o valor da hipotenusa.

'''
# importando biblioteca math do python
import math

colaredPeccary1 = float(5)
colaredPeccary2 = float(10)

'''
math.sqrt é uma função da biblioteca,
math que tira a raiz quadrada de um numero.
'''

hypotenuse = math.sqrt(colaredPeccary1**2 + colaredPeccary2**2)

# formatando o numero para mostrar apenas dois numero depois do ponto.
print('Value of the hypotenuse is: {:.2f}'.format(hypotenuse))
