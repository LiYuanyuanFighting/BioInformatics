The new knowledge about python used:  
1. [dictionary](https://www.tutorialspoint.com/python/python_dictionary.htm)  
e.g  hsa_seq = {}  
     hsa_seq[miRNA_name] = line.replace("\n", "")  
     here hsa_seq is a dictionary, key is miRNA_name  
To use mutiple values for the same key, can use a list as value,  
e.g tag_info=[]  
    tag_info.append(fields[1])  
    tag_info.append(fields[6])  
    tag_info.append(shift)  
    tagIndex_shift[fields[0]] = tag_info  
2. find the index of a string appeared in the other string  
e.g  index = line.find(seed)  

3. convert between string and integers  
str(NonStringVariable) int(NonIntegerVariable)  
take care that the fields got from the file are strings, so don't use:  
fields[1] == 1, but use fields[1] == "1"  
