"""
while True:
    x = int(input("number1: "))
    y = int(input("number2: "))
    if y == 0:
        print("Error")
        continue
    print(x/y)
    break
"""

"""
while True:
    x = input("Угадай имя: ")
    if x == "Vova":
        print("Угадали")
    else:
        print("Не Угадали!")
    break
"""

"""
c = 0
while True:
    x = input("Угадай имя: ")
    c += 1
    if x == "Vova":
        print("Вы угадали!")
        break
    elif c == 10:
        print("Вы проиграли!")
        break
"""

x = int(input("Введите число: "))

for i in range(1, x + 1):


    print('*'* i)
