from __future__ import print_function
import subprocess
import sys

from termcolor import colored

plus = colored('[+]', 'green')
minus = colored('[-]', 'red')


def execute(*args):
    ret = subprocess.Popen(args).wait()
    if ret != 0:
        print('{} {} exited with {}'.format(minus, args[0], ret))
        sys.exit(-1)
