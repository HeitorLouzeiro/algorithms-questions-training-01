'''
João recebeu seu salário e precisa pagar duas contas atrasadas.
Em razão do atraso, ele deverá pagar multa de 2% sobre cada conta.
Faça um programa que calcule e mostre quanto restará do salário de João.

'''

salary = 1320

acount1 = 200
acount2 = 300

# Method one
# amountFine = acount1 * 1.02 + acount2 * 1.02

# Method two
amountFine = (acount1 + acount2)*1.02

salaryFinal = salary - amountFine

print(salaryFinal)
