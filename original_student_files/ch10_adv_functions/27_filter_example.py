"""
    27_filter_example.py
    Using filter()
"""
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']


def not_ber_months(month):
    return month.lower()[-3:] != 'ber'


filter_obj = filter(not_ber_months, months)
print(list(filter_obj))
