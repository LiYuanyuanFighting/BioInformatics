'''
For the different miRNAs identified by a specific miRNA_id calculates the total number of
tags that have been perfectly aligned on it (Output file: mirna_id mirna_name #mapped_tags)
idea: use dictionary data type, key and value used
'''
from sys import argv

script, readFile, writeFile = argv

target1 = open(readFile, "r")
target2 = open(writeFile, "w")

fields = []
# use dictionary data type to ease life
mirna_id_tags = {}
mirna_id_name = {}

for line in target1:
   fields = line.split("\t")
   if fields[0] != "tag_index":
    if mirna_id_tags.has_key(fields[4]):
        mirna_id_tags[fields[4]] += int(fields[15])
    else:
       mirna_id_tags[fields[4]] = int(fields[15])
       mirna_id_name[fields[4]] = fields[5]
      
line = ""  
i = 0
for key in mirna_id_tags:
    line += key+"\t"
    line += mirna_id_name[key]+"\t"
    line += str(mirna_id_tags[key])+"\t"
    # for testing
    i += 1
    if i < 5:
    	print key, "\t", mirna_id_name[key], "\t", mirna_id_tags[key]
    target2.write(line+"\n")
    
target1.close()
target2.close()
      
