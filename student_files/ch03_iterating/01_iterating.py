"""

    01_iterating.py

"""


class MyIterable:
    def __init__(self, min: int = 0, max: int = 5):
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


for i in MyIterable():
    print(i, end=' ')
