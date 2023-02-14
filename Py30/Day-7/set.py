# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
it_companies.update({'h', 'e', 'y'})
print(it_companies)
print(it_companies.remove('IBM'))
print(it_companies.discard("Oracle"))
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(B.union(A))
print(A.symmetric_difference(B))
del it_companies, A, B
ageSet = set(age)
print(len(age), len(ageSet))
a = set("I am a teacher and I love to inspire and teach people".split(" "))
print(len(a))
