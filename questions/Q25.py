'''
Faça um programa que receba uma hora
(uma variável para hora e outra para minutos),
calcule e mostre:
a) a hora digitada convertida em minutos;
b) o total dos minutos, ou seja,
os minutos digitados mais a conversão anterior;
c) o total dos minutos convertidos em segundos.
'''

hours = 10
minutes = 350

hoursMinutes = hours * 60
totalMinutes = minutes + hoursMinutes
minutesSeconds = totalMinutes * 60
print(f'Hours typed {hours} minutes stayed : {hoursMinutes}')
print(f'Total minutes with previously entered time {totalMinutes}')
print('Minutes turned into seconds:', minutesSeconds)
