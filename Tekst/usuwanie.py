import os




delete_list = [' of ',' but ',' to ',' and ',' or ']
with open('Balkan.txt') as fin, open('Balkan_edited', "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, " ")
    fout.write(line)