'''
For the different miRNAs identified by a specific miRNA_id calculates the the ratio between the number of tags mapped onto iso_5p and the number of tags mapped onto the exact miRNA sequence(Output file: mirna_id mirna_name ratio(iso5p/miRNA))
idea: use dictionary data type, key and value used, and store list as value
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
        mirna_id_tags[fields[4]][1] += int(fields[15]) # position 1: mirna exact; 0: iso_5p
        mirna_id_tags[fields[4]][0] += int(fields[16]) 
    else:
       tags = []
       tags.append(int(fields[15]))
       tags.append(int(fields[16]))
       mirna_id_tags[fields[4]] = tags
       mirna_id_name[fields[4]] = fields[5]
      
line = ""  
i = 0
for key in mirna_id_tags:
    line += key+"\t"
    line += mirna_id_name[key]+"\t"
    if mirna_id_tags[key][1] == 0:
       ratio = "unknown"
    else:
    	ratio = mirna_id_tags[key][0]/float(mirna_id_tags[key][1])
    line += str(ratio)+"\t"
    # for testing
    i += 1
    if i < 5:
    	print key, "\t", mirna_id_name[key], "\t", mirna_id_tags[key]
    target2.write(line+"\n")
    
target1.close()
target2.close()
      
