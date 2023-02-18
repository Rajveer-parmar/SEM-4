import functools as ft
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
con = map(lambda x: x.upper(), countries)
print(list(con))
print(list(map(lambda x: x**2, numbers)))
print(list(map(lambda x: x.upper, names)))
print(list(filter(lambda x: 'land' in x, countries)))
print(list(filter(lambda x: len(x) == 6, countries)))
print(list(filter(lambda x: len(x) >= 6, countries)))
print(list(filter(lambda x: x[0] == 'E', countries)))
print(list(map(lambda x: x**2, filter(lambda x: x >= 6, numbers))))
print(list(map(lambda x: x.__str__(), [1, 2, 3, 4, 5, 6])))
