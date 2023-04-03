'''
Faça um programa que receba o número de horas trabalhadas,
o valor do salário mínimo e o número de horas extras trabalhadas,
calcule e mostre o salário a receber, de acordo com as regras a seguir:
a) a hora trabalhada vale 1/8 do salário mínimo;
b) a hora extra vale 1/4 do salário mínimo;
c) o salário bruto equivale ao número de horas trabalhadas multiplicado
pelo valor da hora trabalhada;
d) a quantia a receber pelas horas extras equivale ao
número de horas extras trabalhadas multiplicado pelo valor da hora extra;
e) o salário a receber equivale ao salário bruto
mais a quantia a receber pelas horas extras.

'''
salary = 1320
workedHours = 100  # horas trabalhadas
overtime = 10  # horas extras

valueHours = salary / 8  # valor da hora trabalhada
valueovertime = salary / 4  # valor da hora extra

amountReceivable = (workedHours * valueHours) + \
    (overtime * valueovertime)  # valor a mais que ira receber
# somando o valor do salario com o valor que ira receber
salaryReceivable = salary + amountReceivable

print('Salary to be received is: R$', salaryReceivable)
