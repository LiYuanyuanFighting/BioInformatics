'''
Given a tag file named tags.txt and a file storing all the known miRNAs sequences named
mirna.fa, write a python program that:
(1) For each human miRNA (labeled as hsa within mirna.fa file) identifies the seed sequence and check its presence in the provided tags (stored in tags.txt file)
(2) If the seed is found in the tag in an allowed position (start seed position on the tag between index 0 and 4 included), prints on a file 
idea: use dictionary data type, key and value used, and use find method to get the index
'''
from sys import argv

script, readFile1, readFile2, writeFile = argv

target1 = open(readFile1, "r")
target2 = open(writeFile, "w")
target3 = open(readFile2, "r")

# use dictionary data type to ease life
hsa_seq = {}
flag = False
miRNA_name = ""

for line in target1:
   if line.startswith(">"):
     if line.startswith(">hsa"):
       miRNA_name = line.replace("\n", "")
       flag = True
     else:
       flag = False
   elif flag == True:
     hsa_seq[miRNA_name] = line.replace("\n", "")
    
for key in hsa_seq:
    seed = hsa_seq[key][1:7]
    for line in target3:
       index = line.find(seed)
       if index >= 0 and index <4:
       	  fields = line.split("\t")
          tag_seq = fields[0]
          match = key + "\t" + hsa_seq[key] + "\t" + tag_seq + "\t" + str(index)
          #print "tag_seq:", tag_seq
          #print "str(index):", str(index)
	  target2.write(match+"\n")

   
target1.close()
target2.close()
target3.close()
