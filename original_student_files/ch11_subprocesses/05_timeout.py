import subprocess
import sys

print('\nExample using timeout argument')

result = None
try:
    result = subprocess.run(args=['python', 'sample2.py'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            check=True,
                            timeout=3)
except subprocess.CalledProcessError as err:
    print(f'Error occurred on external process: {err}', file=sys.stderr)
except subprocess.TimeoutExpired as err:
    print(f'Timeout on external process: {err}', file=sys.stderr)

if result:
    print(f'The program said: {result.stdout}')
