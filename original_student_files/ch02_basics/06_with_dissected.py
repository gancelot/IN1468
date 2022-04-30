"""

    Customized example of using the 'with' control

"""
import os


class SetWorkingDir:
    def __init__(self, temp_wd):
        self.new_wd = self.orig_dir = os.getcwd()
        if os.path.exists(temp_wd):
            self.new_wd = temp_wd

    def __enter__(self):
        os.chdir(self.new_wd)
        return os.getcwd()

    def __exit__(self, typ, value, traceback):
        os.chdir(self.orig_dir)


print(f'Before: {os.getcwd()}')
with SetWorkingDir('..') as temp_wd:
    print(f'During: {os.getcwd()}')
    print(open('temp.py', encoding="utf-8").readlines())
print(f'After: {os.getcwd()}')
