"""
        task12_1_starter.py  -   Threaded subprocess Pinger

        This task uses the operating system ping utility via a subprocess within Python.
        It detects your operating system and selects the appropriate command format.

        In this version, it creates a thread for each address to ping.
"""
import subprocess
import sys
import threading


cmds = {'win32': 'ping', 'darwin': 'ping -c 4', 'linux': 'ping -c 4', 'linux2': 'ping -c 4'}
command = cmds.get(sys.platform).split()


def ping(address):
    ping_command = command.copy()
    ping_command.append(address)
    print(f'Ping using: {ping_command}')
    result = subprocess.run(args=ping_command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if not result.returncode:
        print(result.stdout)
    else:
        print('Error: ', result.stdout, file=sys.stderr)
        print(result.stderr, file=sys.stderr)


addresses = ['www.google.com', 'www.cisco.com', 'www.im_a_fake_address.com']
for addr in addresses:
    threading.Thread(target=ping, args=(addr,)).start()
