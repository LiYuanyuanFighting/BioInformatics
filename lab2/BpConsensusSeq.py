from sys import argv
import itertools

def findHighest(base, count):
	maxIndex = 0
	c = 0
	for co in count:
	 if  co > c:
	   c = co
	   maxIndex = count.index(c)
	return base[maxIndex]
	
def reverseList(seqL):
	rList = []
	for s in seqL:
	  rList.append(s[::-1])
	return rList
	
def findConsensus(sequence):
 i = 0
 out = []
 finish = False
 print len(sequence)
 while finish == False:
  limit = 0
  base = []
  count = []
  for seq in sequence:
   if i < len(seq) and seq[i] != "\n": # don ignore \n
    flag = True
    print seq[i]
    for b in base:
     if seq[i] == b:
     	index = base.index(b)
     	count[index] += 1
   	flag = False
    if flag:
     base.append(seq[i])
     count.append(1)
   else:
    limit += 1
    # print limit
    if limit == len(sequence):
   	finish = True
  # get the highest voting base then store into out list
  if finish != True:
   b = findHighest(base, count)
   print "Base is :", b
   out.append(b)
   i += 1
  #print i
 return out

script, readFile = argv

target1 = open(readFile, 'r')

seqL = []
seqR = []
# split and store sequences
for line in target1:
	seqs = line.split("|")
	seqL.append(seqs[0])
	seqR.append(seqs[1])

outR = findConsensus(seqR)
# cz it starts from the breakpoint, so should reverse the left part
temp = reverseList(seqL)
temp2 = findConsensus(temp)
# outL = reverseList(temp2) #error cz this is list, not String
temp2.reverse()
print temp2

# combine 2 list into a string with | as separator
# 1st convert list into string
str1 = ''.join(outR)
print str1
str2 = ''.join(temp2)
print str2

strAll = str2 +'|'+str1
print strAll
'''
 
'''

target1.close()
# target2.close()from sys import argv
import itertools

def findHighest(base, count):
	maxIndex = 0
	c = 0
	for co in count:
	 if  co > c:
	   c = co
	   maxIndex = count.index(c)
	return base[maxIndex]
	
def reverseList(seqL):
	rList = []
	for s in seqL:
	  rList.append(s[::-1])
	return rList
	
def findConsensus(sequence):
 i = 0
 out = []
 finish = False
 print len(sequence)
 while finish == False:
  limit = 0
  base = []
  count = []
  for seq in sequence:
   if i < len(seq) and seq[i] != "\n": # don ignore \n
    flag = True
    print seq[i]
    for b in base:
     if seq[i] == b:
     	index = base.index(b)
     	count[index] += 1
   	flag = False
    if flag:
     base.append(seq[i])
     count.append(1)
   else:
    limit += 1
    # print limit
    if limit == len(sequence):
   	finish = True
  # get the highest voting base then store into out list
  if finish != True:
   b = findHighest(base, count)
   print "Base is :", b
   out.append(b)
   i += 1
  #print i
 return out

script, readFile = argv

target1 = open(readFile, 'r')

seqL = []
seqR = []
# split and store sequences
for line in target1:
	seqs = line.split("|")
	seqL.append(seqs[0])
	seqR.append(seqs[1])

outR = findConsensus(seqR)
# cz it starts from the breakpoint, so should reverse the left part
temp = reverseList(seqL)
temp2 = findConsensus(temp)
# outL = reverseList(temp2) #error cz this is list, not String
temp2.reverse()
print temp2

# combine 2 list into a string with | as separator
# 1st convert list into string
str1 = ''.join(outR)
print str1
str2 = ''.join(temp2)
print str2

strAll = str2 +'|'+str1
print strAll
'''
 
'''

target1.close()
# target2.close()
