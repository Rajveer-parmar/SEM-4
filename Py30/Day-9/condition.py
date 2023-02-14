# if int(input('enter age')) > 18:
#     print('You are old enough to learn to drive.')
# else:
#     print('You need 3 more years to learn to drive.')
# 2

# age = int(input('enter age'))
# if age > 18:
#     print("you are {} older than me".format(age-18))
# else:
#     print("i am {} older than you".format(18-age))
# 3
# a = int(input("enter the a value"))
# b = int(input("enter the b value"))
# print('{} is is greater than {}'.format(a, b)) if a > b else print(
#     "{} is greater than {}".format(b, a))

# 4

# avg = int(input('enter mark'))
# if avg < 40:
#     print('f')
# elif 50 <= avg <= 59:
#     print('d')
# elif 60 <= avg <= 69:
#     print('c')
# elif 70 <= avg <= 89:
#     print('b')
# elif 80 <= avg <= 100:
#     print('a')

# 5

# month = input('enter month')
# if month in ['September', 'October', ' November']:
#     print("Autumn")
# elif month in ['December', 'January ', 'February']:
#     print('Winter')
# elif month in ['March', 'April ', 'May']:
#     print('Spring')
# elif month in ['June', 'July', 'August']:
#     print('Summer')

#  6

# fruits = ['banana', 'orange', 'mango', 'lemon']
# f = input('enter the name of fruit')
# if f in fruits:
#     print('That fruit already exist in the list')
# else:
#     fruits.append(f)

# 7

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# if person['skills']:
#     print(person['skills'][len(person['skills'])//2])
# if person['is_marred']:
#     print(
#         f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is marred")
