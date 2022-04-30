import subprocess
import sys


# Note: replace python, below, with what is appropriate for you...python3, python3.9, etc...
result = subprocess.run(['python', 'sample.py'])   # this will randomly return non-zero occassionally

try:
    result.check_returncode()
except subprocess.CalledProcessError as err:
    print(f'Error running command: {err}', file=sys.stderr)
