# Известен вес боксера-любителя (целое число). Известно, что вес таков, что
# боксер может быть отнесён к одной из трех весовых категорий:
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
#  в какой категории будет выступать данный боксер
weight = int(input())
if weight < 60:
    print('Легкий вес')
elif 60 <= weight < 64:
    print('Первый полусредний вес')
elif 64 <= weight < 69:
    print('Полусредний вес')