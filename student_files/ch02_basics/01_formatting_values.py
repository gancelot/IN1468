"""

    Formatting Examples

"""
employee = ['Bill', 'Smith', 37]
results = 'Name: {0} {1}, age: {2}'.format(*employee)
print(results)


def show_name():
    return ' '.join(employee[:2])


print(f'Name: {show_name()}, age: {employee[2]:0.2f}')
