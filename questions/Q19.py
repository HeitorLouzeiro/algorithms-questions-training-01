'''
sabe-se que, para iluminar de maneira correta os cômodos de uma casa,
para cada m2, deve-se usar 18 W de potência.
Faça um programa que receba as duas dimensões de um cômodo (em metros),
calcule e mostre a sua área (em m2)
e a potência de iluminação que deverá ser utilizada.

'''

length = 20  # comprimento
width = 10  # largura

area = length * width

power = area * 18

print('Room area: ', area, 'square meters')  # area do comodo
# potencia necessaria para iluminar o comodo inteiro.
print('Required power: ', power)
