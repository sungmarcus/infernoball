# Scripts Description

## Individual Practicals

- 5char_mask.sh & gen_mask_wl.sh: This executed the maskprocessor to create a dictionary of words given the masks
- command_line_tools.txt: This is some of the command line tools I used to manipulate text files (sed, awk, grep)
- counter.py: takes in a file and prints how many times a each line appears
- gen_mask_arg.py: This generated a file containing all the JTR commands to perform a mask attack because JTR does not have a multiple mask attack mode
- gen_pbk.sh: This changed a file containing pbk hashes to suit the format of hashcat
- gen_pot.sh: This joined all the pot files (files containing cracked passwords) from hashcat, JTR and created or updated into a master list, it also updated the potfiles of hashcat and johntheripper with the new master pot
- mask_gen.py: This generated a file containing all the mask combinations given the parameters set inside, this was used for generating the 5 char words
- perm.sh: this took two dictionaries of 4 letter words and combined each word to a form a list of compound words with no duplicates
-  password-analyzer.py: this analyses a list of passwords and outputs some stats (gotten online)
- pwl.sh: this generated a dictionary from JTR potfile
- scp_copy.py: This automated copying files from an instance using scp
- scp_send.py: This automated sending files to an instance using scp
- sort_sub: This produced the file needed to submit to submitty, it puts the hashes in suitable format (getting rid of : and spaces) and makes sure that the des was in the right format (due to the bug mentioned in the assignment specs)

## Group Project

- decrypt_cipher.py: This decrypted the cipher to get the next layer using the secret of the current layer 
- get_secret.py: This took in the shares, hashes and passwords to create a secret, it printed the secret generated using k passwords and k-1 passwords provided, if the secret was the same then it meant the secret was correct
- sort_hashes.py: This took in the hashes file and separated into multiple files by the hash type
- split_json.py: this split the json of the layer into its individual parts (shares, hashes, ciphertext and easter egg)
- split_txt.py: This was used to split the dante inferno txt into individual words and output a dictionary
