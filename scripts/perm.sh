cat ~/code/dics/words_4.txt ~/code/dics/words_4.txt | perl -lne 'BEGIN{@a}{push @a,$_}END{foreach $x(@a){foreach $y(@a){print $x.$y}}}' > combined4.txt
sort combined4.txt > combined4sort.txt
awk '!seen[$0]++' combined4sort.txt > tmp && mv tmp combined4sort.txt
mv combined4sort >combined4.txt

