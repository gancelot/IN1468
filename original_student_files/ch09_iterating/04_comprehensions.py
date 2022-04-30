# dictionary comprehension
data = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30,
        'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

day31_months = {k: data[k] for k in data if data[k] > 30}
print(day31_months)


# set comprehension
days_set = {days for days in data.values()}

print(days_set)


# list comprehension
lc = [k for k in range(55) if k % 5 == 0]
# generator expression
ge = (k for k in range(55) if k % 5 == 0)

for val1, val2 in zip(ge, lc):
    print(val1, val2)
