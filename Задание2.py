# Заполнить вручную файл числами ( через пробел в одну строчку ). Создать массив, заполнив его числами из файла

"""Сначала я создаю текстовый файл и добавляю его в PyCharm"""

import re

with open("Задание1.txt", "r") as f:
    text = f.readline()
    ls = text.split(" ")
   # print(ls)
N = []

# for i in range(len(ls)):
