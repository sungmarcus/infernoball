line_st = "aeiou,bcdfghjklmnpqrstvwxyz,"
v = "?1"
c = "?2"
from itertools import permutations
finallist = list()
finallist += [''.join(p) for p in permutations([v,c,c,c,c])]
finallist += [''.join(p) for p in permutations([v,v,c,c,c])]
finallist += [''.join(p) for p in permutations([v,v,v,c,c])]
finallist += [''.join(p) for p in permutations([v,v,v,v,c])]
finallist = list(set(finallist))
finallist = [line_st+s for s in finallist]
print (finallist)

import sys
if __name__ == "__main__":
    filepath = sys.argv[1]
with open(filepath, 'w') as f:
    for item in finallist:
        f.write("%s\n" % item)

