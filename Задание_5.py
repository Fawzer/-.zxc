import random
import my_def
import math

weather_month = []
length = 365

for i in range(length):
    temperature = random.randint(-10, 40)
    weather_month.append(temperature)

print(weather_month)
average = my_def.avg(weather_month)
print("Среднее арифметическое ⬇ ")
print(round(average, 2))

print("Наименьшая температура ⬇ ")
min_temp = my_def.my_min(weather_month)
print(min_temp)

print("Наибольшая температура ⬇ ")
max_temp = my_def.my_max(weather_month)
print(max_temp)
