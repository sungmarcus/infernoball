import sys

if __name__ == "__main__":
    filepath = sys.argv[1]

with open(filepath) as f:
    lines = f.read().splitlines()
strL = "".join(lines)
from collections import Counter
print(Counter(strL))
