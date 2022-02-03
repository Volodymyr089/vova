"""
x = []

while True:
    y = input("Введите гостей в список: ")
    if y == "Все":
        break
    x.append(y)
print("Вечеринка началась!")
while True:
    c = input("Введите имя гостя: ")
    if c in x:
        print(c, "есть в списке")
        x.remove(c)
    else:
        print("Нет в списке!")
    if len(x) == 0:
        break
print("Все гости на месте!")
"""

clothes = []
counter = 0
while True:
    x = input("Что вы купили: ")
    if x == "Все":
        break
    y = int(input("Цена товара:"))

    clothes.append(x)
    counter += y
print("Список: ", clothes)
print("Сумма: ", counter)

