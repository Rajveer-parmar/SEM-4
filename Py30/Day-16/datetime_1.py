import datetime as d
date = d.datetime.now()
print(date)
print(date.strftime("%m/%d/%Y, %H:%M:%S"))
print(d.strptime(date, "%d/%m/%y"))
print(date.year-datetime(2024))
