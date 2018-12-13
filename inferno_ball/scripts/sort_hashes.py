import sys

if len(sys.argv) < 1:
    print("Specify an input path for the hashes file.")
else:   
    input_path = sys.argv[1]
    with open(input_path, "r" ) as hashes_file:
        hashes = hashes_file.readlines()
        sha1= []
        sha512 = []
        pbkdf2 = []
        argon2 = []
        for hash in hashes:
            if "$sha1$480000$" in hash:
                sha1.append(hash)
            elif "$pbkdf2" in hash and len(hash) == 88:
                pbkdf2.append(hash)
            elif "$argon2i$" in hash and len(hash) == 77:
                argon2.append(hash)
            else:
                sha512.append(hash)

        hashes_detected =  len(sha1) + len(sha512) + len(pbkdf2) + len(argon2)
        all_hash_types_detected = len(hashes) == hashes_detected

        if all_hash_types_detected:
            print("All %i hashes were successfully identified by their respective algorithms." % len(hashes))
        else:
            unknown_hashes = len(hashes) - hashes_detected
            print("Could not identify the algorithms of %i hashes." % unknown_hashes)
        stat = []
        stat.append("SHA1: %i" % len(sha1)+"\n")
        
        stat.append("SHA-512: %i" % len(sha512)+"\n")
        stat.append("PBKDF2: %i" % len(pbkdf2)+"\n")
        stat.append("Argon 2: %i" % len(argon2)+"\n")
        print(stat)

        with open("sha1_hashes", "w") as sha1_hashes:
            for h in sha1:
                sha1_hashes.write(h)
        with open("sha512_hashes", "w") as sha512_hashes:
            for h in sha512:
                sha512_hashes.write(h)
        with open("pbkdf2_hashes", "w") as pbkdf2_hashes:
            for h in pbkdf2:
                pbkdf2_hashes.write(h)
        with open("argon2_hashes", "w") as argon2_hashes:
            for h in argon2:
                argon2_hashes.write(h)
        with open("stats","w") as stats:
            for s in stat:
                stats.write(s)
