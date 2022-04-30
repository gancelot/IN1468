import json
import subprocess
import sys

print('Example using Popen')
# be sure to change the line below to python3, python3.10, python3.x,
# or whatever works on your system...
proc = subprocess.Popen(['python', '-V'], text=True,
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
print(f'Your python version: {stdout}')


print('\n\nExample using Popen and the with control')
with subprocess.Popen(['pip', 'list', '--format=json'],
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE,
                      text=True) as proc:
    result = proc.stdout.readlines()

print(f'Is proc stdout closed? {proc.stdout.closed}')
data = json.loads(result[0])
for package in data:
    print(f'{package["name"]}: {package["version"]}')


cmds = {'win32': 'netstat -an', 'darwin': 'netstat -a | grep -i "listen"', 'linux': 'netstat | grep LISTEN', 'linux2': 'netstat | grep LISTEN'}
command = cmds.get(sys.platform)
print('\n\nUsing: ', command)
with subprocess.Popen(command.split(),
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE,
                      text=True) as proc:
    result = proc.stdout.readlines()

print(''.join(result))
