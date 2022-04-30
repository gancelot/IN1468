import subprocess


# subprocess.run(['echo', 'hello'])                # POSIX
subprocess.run(['echo', 'hello'], shell=True)      # Windows
