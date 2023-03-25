import webbrowser as wb
import requests
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]
for i in url_lists:
    wb.open_new_tab(i)
url = 'http://www.gutenberg.org/files/1112/1112.txt'
res = requests.get(url)
print(res)
print(res.status_code)
data = res.text.split()
for i in data.split():
    print(data.count(i))
