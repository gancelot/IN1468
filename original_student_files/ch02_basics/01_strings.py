import linecache
# linecache reads lines from files without returning an error

line = linecache.getline('resources/simpsons.csv', 129).strip()


print(line)                         # 127,Moe Szyslak,Hank Azaria,Owner of Moe's Tavern.,"""Simpsons Roasting on an Open Fire""",1989-12-17
print(line[4])                      # M
print(line[4:15])                   # Moe Szyslak
print(line[:3])                     # 127
print(line[-10:])                   # 1989-12-17
print(line[4:15:2])                 # MeSylk

# find and split
print(line.find('Moe'))             # 4
print(line.find('Homer'))           # -1
print(line.split(','))              # ['127', 'Moe Szyslak', 'Hank Azaria', "Owner of Moe's Tavern.", '"""Simpsons Roasting on an Open Fire"""', '1989-12-17']
print(line.split(',')[2])           # Hank Azaria


# for larger files
print('Example reading a specific line (larger files): ')
with open('../resources/access_.log') as f:
    for idx, line in enumerate(f):
        if idx == 21:
            print(line)
