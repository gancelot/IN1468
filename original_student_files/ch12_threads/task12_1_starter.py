"""
        task12_1_starter.py  -   Threaded subprocess Pinger

        This version of our pinger allows for multiple pings to occur at once
        via the use of threads.  It creates a single thread per address to ping.

        Step 1. Create a function called ping() that accepts an address.

        Step 2. Move the code below into this new function (this is pretty-much what
                we created in the last task)...


    ping_command = command.copy()
    ping_command.append(address)
    print(f'Ping using: {ping_command}')
    result = subprocess.run(args=ping_command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if not result.returncode:
        print(result.stdout)
    else:
        print('Error: ', result.stdout, file=sys.stderr)
        print(result.stderr, file=sys.stderr)



        Step 3. Remove the pass statement.
                Instantiate a Thread object using the Thread() class (refer to the task slide).
                Use the target= attribute and specify your ping function from step 2.
                Supply an args= attribute that passes an address into it.
                Hint:  Refer to the task slide on how to do this.

"""
import subprocess
import sys
import threading


cmds = {'win32': 'ping', 'darwin': 'ping -c 4', 'linux': 'ping -c 4', 'linux2': 'ping -c 4'}
command = cmds.get(sys.platform).split()

# Steps 1 and 2. here

addresses = ['www.google.com', 'www.cisco.com', 'www.im_a_fake_address.com']
for addr in addresses:
    pass
    # Step 3. here
