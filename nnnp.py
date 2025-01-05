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