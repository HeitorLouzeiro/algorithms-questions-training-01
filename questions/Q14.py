'''
Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual,
calcule e mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
d) a idade dessa pessoa em semanas.

'''

yearBirth = int(input('Enter data of birth:'))
yearCurrent = int(input('Enter year current:'))

age = yearCurrent - yearBirth
monthsAge = age * 12
dayAge = monthsAge * 365
weekAge = dayAge / 7

print('\nYou age in')
print('Age:', age)  # Idade em anos
print('Months:', monthsAge)  # Idade em meses
print('Day:', dayAge)  # Idade em dias
print('Week:', weekAge)  # idade em semanas
