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