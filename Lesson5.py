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
"""
"""
x = [1, 5, 4, 3, 9, 8, 10]
nu_min = x[0]
nu_max = x[0]
s = 0
c = 0
for i in x:

    if i < nu_min:
        nu_min = i
    if i > nu_max:
        nu_max = i
    s+=i
    c +=1
print(nu_max)
print(nu_min)
print(s)
print(c)
"""