# Задание № 1. Дан произвольный список. Представьте его в обратном порядке.
import random
arr = [random.randint(1,101) for i in range(10)]
print('созданный список', arr)                       # созданный список с рандомными элементами
arr.sort()
print('отсортированный по возрастанию', arr)                       # отсортированный по возрастанию
arr.reverse()
print('в обратном порядке', arr)                       # в обратном порядке

