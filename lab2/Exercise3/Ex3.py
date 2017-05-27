'''
For each tag that has been mapped on a iso_5p evaluates the shift of the seed sequence
(Output file : tag_index tag_sequence mirna_seq shift:+/-x)
idea: use dictionary data type, key and value used, and use find method to get the index
'''
from sys import argv

script, readFile, writeFile = argv

target1 = open(readFile, "r")
target2 = open(writeFile, "w")

fields = []
# use dictionary data type to ease life
tagIndex_shift = {}

for line in target1:
   fields = line.split("\t")
   if fields[0] != "tag_index" and fields[16] == "1":
      tag = fields[1]
      mirna = fields[6][1:7] # extract the 6 bases
      index = tag.find(mirna)
      if index >= 0:
        shift = index - 1
        tag_info=[]
        tag_info.append(fields[1])
        tag_info.append(fields[6])
        tag_info.append(shift)
        tagIndex_shift[fields[0]] = tag_info
      else:
        print "Failed to find the match"
      
line = ""  
i = 0
for key in tagIndex_shift:
    line += key+"\t"
    line += tagIndex_shift[key][0]+"\t"
    line += tagIndex_shift[key][1]+"\t"
    line += str(tagIndex_shift[key][2])+"\t"
    # for testing
    i += 1
    if i < 5:
    	print key, "\t", tagIndex_shift[key][0], "\t", tagIndex_shift[key][1], tagIndex_shift[key][2]
    target2.write(line+"\n")
    
target1.close()
target2.close()
      
