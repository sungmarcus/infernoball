import sys
import os

if __name__ == "__main__":
    keys = sys.argv[1]
    filetocopy = sys.argv[2]
    vm = sys.argv[3]

from subprocess import call
cmd = "scp -i "+keys+" ubuntu@"+vm+":"+filetocopy+" "+os.getcwd()
call(cmd.split())

