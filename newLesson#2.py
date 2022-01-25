number_1 = int(input('enter your first number: '))
number_2 = int(input('enter your second number: '))
operator = input('input [-,+,/,*]')
if operator == '-':
    print(number_1 - number_2)
elif operator == '+':
    print(number_1 + number_2)
elif operator == '*':
    print(number_1 * number_2)
elif operator == '/':
    if number_2 != 0:
        print(number_1 / number_2)
    else:

        print('Нельзя делить на ноль!')
else:
    print('Не правильный знак!')
