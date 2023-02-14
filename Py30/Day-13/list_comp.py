

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
l = [i for i in numbers if i > 0]
print(l)
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
onr_lst = [i for j in list_of_lists for i in j[0]]
print(onr_lst)
list_of_tuples = [(i, 1, 1*i, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)
new_countries = [[i.upper(), i[:3].upper(), k]
                 for j in countries for i, k in j]
print(new_countries)
new_dict = [{'country': i, 'city': k} for j in countries for i, k in j]
print(new_dict)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_names = [i+" "+k for j in names for i, k in j]
print(new_names)
