# 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

number = int(input('Введите натуральное число: '))
list_of_numbers = []
for i in range(-number,number+1):
    list_of_numbers.append(i)
print(list_of_numbers)
with open("positions.txt","r") as f:
    pos_1 = int(f.readline())
    pos_2 = int(f.readline())
num_1 = list_of_numbers[pos_1 - 1]
num_2 = list_of_numbers[pos_2 - 1]
print(f'Произведение чисел, стоящих на позициях {pos_1} и {pos_2}:')
print(f'{num_1} * {num_2} = {num_1*num_2}')