import subprocess
import sys

print('Example illustrating check=True argument')

result = None
try:
    result = subprocess.run(args=['python', 'sample.py'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            check=True)
except subprocess.CalledProcessError as err:
    print(f'Error occurred on external process: {err}', file=sys.stderr)

if result:
    print(f'The program said: {result.stdout}')
