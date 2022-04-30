import subprocess
import sys


print('Example using pipe= arguments')
result = subprocess.run(args=['python', 'sample.py'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)

print(f'The program said: {result.stdout.decode()}')
if result.returncode:
    print(f'Error message: {result.stderr.decode()}', file=sys.stderr)


print('\nExample using text=True')
result = subprocess.run(args=['python', 'sample.py'],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)

print(f'The program said: {result.stdout}')
if result.returncode:
    print(f'Error message: {result.stderr}', file=sys.stderr)
