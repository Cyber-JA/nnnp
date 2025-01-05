# No netcat ? No problem
import socket
import threading
import argparse
import subprocess
import shlex
import sys
import textwrap

def execute(cmd):
    cmd = cmd.strip()
    if not cmd:
        return
    
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    
    return output.decode()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='No Netcat ? No problem',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
                               nnnp.py -t 10.10.10.10 -p 1234 -l -c # command shell
                               nnnp.py -t 10.10.10.10 -p 1234 -l -u=text.txt # file upload
                               nnnp.py -t 10.10.10.10 -p 1234 -l -e=\"cat /etc/passwd\" # execute command
                               echo something | nnnp.py -t 10.10.10.10 -p 1234" # echo something to specified target
                               nnnp.py -t 10.10.10.10 -p 1234 # connect to target''')
    )
    parser.add_argument('-c', '--command', action='store_true', help='command shell')
    parser.add_argument('-e', '--execute', help='execute specified command')
    parser.add_argument('-l', '--listen',action='store_true', help='listener mode')
    parser.add_argument('-p', '--port', help='specify port to be used', type=int, default=1234)
    parser.add_argument('-t', '--target', help='specify target', default='127.0.0.1')
    parser.add_argument('-u', '--upload', help='upload specified file')
    args = parser.parse_args()

    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    
    nc = nnnp(args, buffer.encode())
    nc.run()

class nnnp:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()
    
    def send():
        pass