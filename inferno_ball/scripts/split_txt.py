import sys
words = []
input_file = sys.argv[1]
with open(input_file,'r') as file:
    for line in file:
        for word in line.split():
            words.append(word)
words = list(set(words))
with open("dante.dic",'w') as out:
    for word in words:
        out.write(word+"\n")

