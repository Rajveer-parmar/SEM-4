dog = {}
dog['name'] = 'Pablo'
dog['color'] = "brown"
dog['breed'] = 'desi'
dog['legs'] = 5
dog['age'] = 5
student = {'first_name': 'pablo', 'last_name': 'escobar', 'gender': 'male', 'age': 36, 'marital status': None,
           'skills': 'drug mafia', 'country': 'UAE', 'city': 'IDK', 'address': "nckejnckjcjdsnchbwer"}
print(len(student))
student['skills'] = ['drug', 'mafia']
print(type(student['skills']))
print(list(student.keys()))
print(list(student.values()))
print(tuple(student.items()))
del student['city']
del dog
