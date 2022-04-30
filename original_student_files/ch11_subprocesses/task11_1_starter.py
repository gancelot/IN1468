"""
        task11_1_starter.py  -   Subprocess pinger

        This task uses the operating system ping utility via a subprocess within Python.
        It detects your operating system and selects the appropriate command format.
        You'll need to add the address to your command and then run subprocess.run().
"""
import subprocess
import sys

cmds = {'win32': 'ping', 'darwin': 'ping -c 4', 'linux': 'ping -c 4', 'linux2': 'ping -c 4'}
command = cmds.get(sys.platform)

address = 'www.google.com'         # if external network access is not possible, use an internal host

# Step 1. Split your 'command' into a list of strings (hint: use .split()

# Step 2. Add the address to your command list.  print() your command to check it.

# Step 3. Call subprocess.run() and display the results
#         (hint: use args=, stdout=, stderr=, and text= arguments)

