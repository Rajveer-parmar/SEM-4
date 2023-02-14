from random import randint as r, choice as c, shuffle


def random_user_id(length):
    import string
    a = r(1, length)
    b = length-a
    ca = ''
    for i in range(a):
        ca += c(string.ascii_letters)
    for i in range(b):
        ca += c(string.digits)
    return ca


def rgb_color_gen():
    return f'rgb{r(0,255),r(0,255),r(0,255)}'


def generate_colors(which_one, how_much):
    import secrets
    l = []
    if which_one == "hex":
        for i in range(how_much):
            l.append("#"+secrets.token_hex(3))
    elif which_one == "rgb":
        for i in range(how_much):
            l.append(rgb_color_gen())

    return l


def suff(l):
    shuffle(l)
    return l


def seven_random():
    l = []
    while len(l) != 7:
        i = r(0, 9)
        if (i not in l):
            l.append(i)
    return l


# n = input("how much user id you want ").split(" ")
# for i in range(int(n[1])):
#     print(random_user_id(int(n[0])))
print(rgb_color_gen())
print(generate_colors('rgb', 3))
print(suff([1, 2, 3, 4, 5]))
print(seven_random())
