"""
        task11_1_solution.py  -   Subprocess pinger

        This task uses the operating system ping utility via a subprocess within Python.
        It detects your operating system and selects the appropriate command format.
        You'll need to add the address to your command and then run subprocess.run().
"""
import subprocess
import sys

cmds = {'win32': 'ping', 'darwin': 'ping -c 4', 'linux': 'ping -c 4', 'linux2': 'ping -c 4'}
command = cmds.get(sys.platform)

address = 'www.google.com'         # if external network access is not possible, use an internal host

command = command.split()
command.append(address)
print('Using: ', command)

result = subprocess.run(args=command, text=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if not result.returncode:
    print(result.stdout)
else:
    print('Error: ', result.stdout, file=sys.stderr)               # ping will likely use stdout for error message too
    print(result.stderr, file=sys.stderr)
