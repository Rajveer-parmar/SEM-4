t = ()
tpl1 = ('h', 'e', 'l', 'l', 'o')
tpl2 = ('w', 'o', 'r', 'l', 'd')
tpl3 = tpl1+tpl2
print(len(tpl3))
family = tpl3+("family", "suuiiii")
print(family)
*a, fam, mab = family
print(fam, mab)
fruits, vegetables, animal = (
    'apple', 'kiwi', 'pineapple'), ('potato', 'tametu', 'ringnu'), ('cat', 'lion', 'tiger')
food_stuff_tp = fruits+vegetables+animal
l = list(food_stuff_tp)
print(food_stuff_tp[len(food_stuff_tp)//2])
print(l[:3], l[-3:])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
