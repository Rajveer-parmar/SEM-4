import json
f = open("data.json", encoding='utf-8')
data = json.load(f)
# print(len(f.split('\n')))
# print(len(f.split()))
# j = json.dumps(f, indent=4)
print(data)
