# Написать программу, которая проверяет правильно ли пользователь
# провел вычисления, если нет, то показывает правильное значение

a = float(input("введите число"))
b = float(input("введите второе число"))
oper = input("введите действие")
if oper == "+":
    d =(a+b)
elif oper == "-":
    d = (a-b)
elif oper == "*":
    d = (a*b)
elif oper == "/":
    d = (a/b)
elif oper == "//":
    d = (a//b)
elif oper == "%":
    d = (a%b)
else:
    print("неправильно ввели что-то")
f = float(input("введите ответ"))
if f == d:
    print("Все верно")
elif f !=d:
    print("Не верно")
    print("Правильный ответ",d)









































































































































































































































































































































































