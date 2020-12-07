import os
import random



delete_list = [' of ',' but ',' to ',' and ',' or ']
replace_list = [' ziemniak ',' marchewka ',' majonez ',' polonez ']
with open('Balkan.txt') as fin, open('Balkan_edited', "w+") as fout:
    for line in fin:
        for word in delete_list:
            
            x = random.choice(replace_list)
            line = line.replace(word, x)
        fout.write(line)