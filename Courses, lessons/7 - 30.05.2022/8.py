# Вам передан массив чисел. Известно, что каждое число в этом массиве имеет
# пару, кроме одного, выведите это число.
arr = [1, 5, 2, 9, 2, 9, 1]
for i in arr:
    if arr.count(i) < 2:
        print(i)