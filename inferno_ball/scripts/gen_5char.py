line_st = "./maskprocessor/src/mp64.bin -1 aeiou -2 bcdfghjklmnpqrstvwxyz -3 0123456789 "
v = "?1"
c = "?2"
d = "?3"
from itertools import permutations
finallist = list()
finallist += [''.join(p) for p in permutations([v,c,c,c,d])]
finallist += [''.join(p) for p in permutations([v,v,d,c,c])]
finallist += [''.join(p) for p in permutations([v,v,v,d,c])]
finallist += [''.join(p) for p in permutations([v,v,v,v,d])]

finallist = list(set(finallist))
##finallist = [line_st+s for s in finallist]
print (finallist)

import sys
if __name__ == "__main__":
    filepath = sys.argv[1]
with open(filepath, 'w') as f:
    for item in finallist:
        f.write("%s\n" % item)

