'''
Faça um programa que calcule e
mostre a tabuada de um número digitado pelo usuário.
Exemplo: Digite um número:

5 5 * 0 = 0
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

'''

number = int(input('Enter a number:'))

for i in range(1, 10+1):
    mult = number * i
    print(f'The {number} x {i} = {mult}')
