"""
    28_any_all.py
    Using any() and all()
"""
months = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

print(all(len(mo) < 10 for mo in months))
print(any(len(mo) > 8 for mo in months))
