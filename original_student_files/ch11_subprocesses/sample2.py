import random
import sys
import time

print('This is sample.py')
ret_val = random.randint(0, 1)
if ret_val:
    time.sleep(4)
    print('A random error occurred.', file=sys.stderr)

sys.exit(ret_val)
