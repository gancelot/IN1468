#---------------------------------------
#   Formatting examples
#
print('The following are examples of using the format() method:')
employee = ['Bill', 'Smith', 37]
fmt_results = '{0} {1} {2}'.format(*employee)
print(fmt_results)

employee = ['Bill', 'Smith', 37]
fmt_results = '{0:-^20} {1:-<30} {2:>8}'.format(*employee)
print(fmt_results)

employee = {'first': 'Bill', 'last': 'Smith', 'age': 37}
fmt_results = '{fst: ^20} {lst: <30} {age:>8}'.format(fst=employee['first'], lst=employee['last'], **employee)
print(fmt_results)

employee = {'first': 'Bill', 'last': 'Smith', 'age': 37}
fmt_results = '{first: ^20} {last: <30} {age:>8}'.format(**employee)
print(fmt_results)

employee = {'first': 'Bill', 'last': 'Smith', 'age': 37}
col_widths = [20, 30, 8]
fmt_results = '{first: ^{0}} {last: <{1}} {age:>{2}}'.format(*col_widths, **employee)
print(fmt_results)


# Example using f-strings...
first = 'Bob'
last = 'Smith'
age = 37


def show_name():
    return first + ' ' + last


print(f'{first} {last} {age:0.2f} {show_name()}')