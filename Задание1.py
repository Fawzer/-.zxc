# Сгенерировать массив из N случайных чисел. Записать полученный масив в файл
# install random

import random

N = []

print("Данный цикл расчитан на колличесво элеметов которое не привышает 10.000.000")
amount_of_numbers = int(input("Введите колличество элементов которое будет в массиве - "))
if amount_of_numbers > 1000000:
    print("(╯°□°）╯ Число не может быть таким большим, (ಠ_ಠ)☭. Попробуйте попытку перезапустив цикл")
    exit("           🤬нарушение условий🤬     ")
if amount_of_numbers <= 0:
    print("(╯°□°）╯ Число не может ровняться нулю и быть меньше нуля , (ಠ_ಠ)☭. Попробуйте попытку перезапустив цикл")
    exit("           🤬нарушение условий🤬     ")

for i in range(amount_of_numbers):
    num = random.randint(-100000000, 100000000)
    N.append(num)

outStr = ""
for i in range(len(N) - 1):
    outStr = outStr + str(N[i]) + " "
outStr = outStr.strip()

with open('Задание1.txt', 'w') as f:
    f.write(outStr)

print(N)
