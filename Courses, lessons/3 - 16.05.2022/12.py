# Напишите программу для нахождения цифр четырёхзначного числа.
a = int(input())
b = a % 10
c = (a % 100) // 10
d = (a % 1000) // 100
e = a // 1000
print('Цифра в позиции тысяч равна', e)
print('Цифра в позиции сотен равна', d)
print('Цифра в позиции десятков равна', c)
print('Цифра в позиции единиц равна', b)
