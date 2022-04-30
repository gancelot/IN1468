class Something:
    def __init__(self, min=0, max=5):
        self.count = min
        self.min = min
        self.max = max

    def __next__(self):
        val = self.count
        self.count += 1
        if self.count > self.max:
            raise StopIteration
        return val

    def __iter__(self):
        self.count = self.min
        return self

s = Something()
for i in s:
    print(i, end=' ')
    if i == 3:
        break

print()
for i in s:
    print(i, end=' ')

print()
s1 = Something(2, 5)
s2 = Something(10, 13)
for i in s1:
    print(i)
    for j in s2:
        print(j, end=' ')
    print()

