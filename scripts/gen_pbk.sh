#!/bin/bash
sed -i 's/:/ /g4' ./final_hashes/pbkdf2.txt
sed -i 's/:/$/g' ./final_hashes/pbkdf2.txt
sed -i 's/ /:/g' ./final_hashes/pbkdf2.txt
sed -i 's/^/$pbkdf2-/' ./final_hashes/pbkdf2.txt

