import sys
if __name__ == "__main__":
    keys = sys.argv[1]
    filetosend = sys.argv[2]
    vm = sys.argv[3]

from subprocess import call
cmd = "scp -i "+keys+" "+filetosend+" ubuntu@"+vm+":"
call(cmd.split())

