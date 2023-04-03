'''
Faça um programa que receba a quantidade de dinheiro
em reais que uma pessoa que vai viajar possui.
Ela vai passar por vários países e precisa converter seu dinheiro em dólares,
marco alemão e libra esterlina.
sabe-se que a
cotação do dólar é de R$ 1,80;
do marco alemão, de R$ 2,00;
e da libra esterlina, de R$ 3,57.
O programa deve fazer as conversões e mostrá-las.
'''

value = 25000

valueDollar = value * 1.80
valueGerman = value * 2
valueSterling = value * 3.57

print('Its value in')
print('Dollar:', valueDollar)
print('German:', valueGerman)
print('Sterling', valueSterling)
