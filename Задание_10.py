# 4 задание из телеграмма
print("Вы вводите число от 0 до 1000 и программа вам выдает из скольких разрядов оно состоит")

while True:
    try:
        number = int(input("Введите число➥ "))
        break
    except ValueError:
        print("(╯°□°）╯ По условию число не можеть быть типом файлов STR (ಠ_ಠ)☭. Try again...")
        exit("           🤬нарушение условий🤬     ")
if number < 0:
    print("(╯°□°）╯ По условию число не можеть быть меньше нуля (ಠ_ಠ)☭. Try again...")
    exit("           🤬нарушение условий🤬     ")
if number > 1000:
    print("(╯°□°）╯ По условию число не можеть быть больше тысячи (ಠ_ಠ)☭. Try again...")
    exit("           🤬нарушение условий🤬    ")

# if number / 1 == number // 1:
#     print("Число одно разрядное")
# else:
#     if number / 10 == number // 10:
#         print("Число двух разрядное")
#     else:
#         if number / 100 == number // 100:
#             print("Число трех разрядное")


if number / 100 == number // 100:
    print("Число трех разрядное")
else:
    if number / 10 == number // 10:
        print("Число двух разрядное")
    else:
        if number / 1 == number // 1:
            print("Число одно разрядное")
