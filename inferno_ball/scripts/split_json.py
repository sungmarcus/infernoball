import json
import sys

input_file = sys.argv[1]
with open(input_file,'r') as f:
    json_dict = json.load(f)

hashes_list = (json_dict['hashes'])
shares_list = (json_dict['shares'])
with open('all_hashes', 'w') as f:
    for item in hashes_list:
        f.write("%s\n" % item)

with open('cipher', 'w') as f2:
    f2.write(json_dict['ciphertext'])

with open('shares', 'w') as f3:
    for item in shares_list:
        f3.write("%s\n" % item)
with open('easter_egg', 'w') as f4:
        f4.write(json_dict['easteregg'])

