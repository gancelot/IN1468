import random
import sys

print('This is sample.py')
ret_code = random.randint(0, 1)
if ret_code:
    print('A random error occurred.', file=sys.stderr)

sys.exit(ret_code)       # ret_code will be 0 or 1
