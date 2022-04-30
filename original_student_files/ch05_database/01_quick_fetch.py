import sqlite3

conn = sqlite3.connect('course_data.db')
cursor = conn.cursor()
cursor.execute('select fullname, city, state from schools where state="CO"')
results = cursor.fetchmany(size=3)
print(results)
