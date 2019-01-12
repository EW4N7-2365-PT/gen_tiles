from __future__ import print_function
import subprocess
import sys
from termcolor import colored

plus = colored('[+]', 'green')
minus = colored('[-]', 'red')


def execute(program, *args):
    ret = subprocess.Popen([program, args]).wait()
    if ret != 0:
        print('{} {} exited with {}'.format(minus, program, ret))
