#!/bin/bash
cut -d: -f2 ~/code/JohnTheRipper/run/john.pot | sort -u > ~/code/pot.dic
awk '{print length, $0}' ~/code/pot.dic | sort -n | cut -d " " -f2- > ~/code/pots.dic
