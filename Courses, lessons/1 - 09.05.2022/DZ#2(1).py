# Определить является ли год високосным

a = int(input("Введите год"))
if a % 4 == 0:
    print("Высокосный год")
else:
    print("Невысокосный год")