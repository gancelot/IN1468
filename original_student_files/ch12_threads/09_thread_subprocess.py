import threading
import subprocess
import sys

external_process_cmd = r'dir .'
# external_process_cmd = r'ls -l ~'


class ExternalCommandThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stdout = None
        self.stderr = None

    def run(self):
        p = subprocess.Popen(external_process_cmd.split(),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             text=True)

        self.stdout, self.stderr = p.communicate()

extCmd = ExternalCommandThread()
extCmd.start()
extCmd.join()
print(extCmd.stdout)
print(extCmd.stderr, file=sys.stderr)
