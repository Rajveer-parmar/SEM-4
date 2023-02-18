import re


def is_valid_variable(s):
    return bool(re.search(r'^[^a-z]', s))


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# a = set(paragraph.split(' '))
# l = [(len(re.findall(i, paragraph, re.I)), i) for i in a]
# print(l)

# points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
# points_new = [int(i) for i in points]
# sorted_points = [-4, -3, -1, -1, 0, 2, 4, 8]
# l1 = [i-j for i in points_new for j in sorted_points]

# print(max(l1))
# print(is_valid_variable("first"))
d = ''
for i in ["%", '@', "$", '&', ';', '!', "#"]:
    sentence = re.sub(i, '', sentence)
print(sentence)
