#!/bin/bash
cp gen.pot ~/code/final_hashes/sungm.broken
sed -i -e 's/:/ /g' ~/code/final_hashes/sungm.broken
sed -i 1,334d ~/code/final_hashes/sungm.broken
cat ~/code/final_hashes/cracked_des_final.txt ~/code/final_hashes/sungm.broken > ~/code/final_hashes/sungm.sorted; mv ~/code/final_hashes/sungm.sorted ~/code/final_hashes/sungm.broken
