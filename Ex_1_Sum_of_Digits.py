number = str(input('Введите число: '))
def SumDigit(num):
    num = num.replace(',','')
    num = num.replace('.','')
    num = num.replace('-','')
    sum = 0
    for i in range(len(num)):
        sum = sum + int(num[i])
    return sum
sum = SumDigit(number)
print(f'Сумма цифр числа {number} равна {sum}')