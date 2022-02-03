x = []

while True:
    y = input("Введите гостей в список: ")
    if y == "Все":
        break
    x.append(y)

while True:
        c = input("Введите имя гостя: ")
        if c in x:
            print(c,  "есть в списке")
        else:
            print("Нет в списке!")
