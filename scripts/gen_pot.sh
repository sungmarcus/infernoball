#!/bin/bash
cat ./JohnTheRipper/run/john.pot >> gen.pot
cat ./hashcat/hashcat.potfile >> gen.pot
cat hashcat.potfile >> gen.pot
awk '!seen[$0]++' gen.pot > tmp && mv tmp gen.pot
awk '{print length, $0}' gen.pot | sort -n | cut -d " " -f2- > gen_sort.pot
cp gen_sort.pot gen.pot
cp gen.pot ./JohnTheRipper/run/john.pot
cp gen.pot ./hashcat/hashcat.potfile
cp gen.pot hashcat.potfile
