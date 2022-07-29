import random

count = int(input("Введите колличесво элементов в массиве - "))
if count == str:
    exit("Число а не букву!!")

A = list()
B = []
C = set()

for i in range(count):
    num1 = random.randint(0, 100)
    A.append(num1)
    num2 = random.randint(0, 100)
    B.append(num2)

# print(A)
# print(B)

for i in range(count):
    isSet = True
    for j in range(count):
        if A[i] == B[j]:
            isSet = False
            break
    if isSet:
        C.add(A[i])

    isSet = True
    for j in range(count):
        if B[i] == A[j]:
            isSet = False
            break
    if isSet:
        C.add(B[i])

print(C)






