# This version fails (and is commented out because of it)
# def outer_function():
#     x = 3
#
#     def my_closure():
#         x += 1
#         print(x)
#
#     my_closure()
#
#
# outer_function()


# This version works...
# comment out the one above and uncomment the one below to test it out

def outer_function():
    x = [3]

    def my_closure():
        x[0] += 1
        print(x[0])

    my_closure()


outer_function()


# This last version also works and uses the keyword, nonlocal.
# It presents an ideal way to go with this implementation
def outer_function():
    x = 3

    def my_closure():
        nonlocal x
        x += 1
        print(x)

    my_closure()


outer_function()
