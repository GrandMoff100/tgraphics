import sys
import colorama
import threading

from .readchar import readkey

class Stdout:
    data = ''
    stdout = sys.stdout

    def write(self, content):
        Stdout.data += content
        Stdout.stdout.write(content)

    def read(self):
        return Stdout.data
    
    def clear(self):
        Stdout.data = ''
        colorama.init()
        print(colorama.ansi.clear_screen(), end='', flush=True)
