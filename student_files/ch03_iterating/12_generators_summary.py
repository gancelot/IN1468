# summary of generator behaviors (can and cannot do)....
def my_generator():
    values = [1, 2, 3]
    for i in values:
        yield i


# things you cannot do...
# print(my_generator())       # this doesn't behave like a function
# print(my_generator()[0])
# print(len(my_generator()))

# 4 ways to invoke (work with) a generator...
# 1
for i in my_generator():
    print(i)

# 2
results = list(my_generator())
print(results)

# 3
print(*my_generator())

# 4
g = my_generator()
print(g.__next__())
print(next(g))
print(next(g))

# You can...
if 1 in my_generator():
    print('it\'s there!')
