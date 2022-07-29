word = input("Введите целое число - ")
length = len(word)
is_palindrome = True

for i in range(length):
    if word[i] != word[length - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Это палиндром")
else:
    print("Это не палиндром")

