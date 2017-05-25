
import textwrap
from sys import argv

def extract(start, end, buffer):
 
 preLine = ""
 sequence = ""
 preFlag = True
 count = 0
 
 for line in buffer:
   if count >= start:
   
    if preFlag:
      preLen = count - BPtm 
      print preLen
      temp = len(line)
      gap = preLen
      print gap
      k = 0
      while preFlag:
       if gap > temp:
         j = 0
       else:
         j = temp - gap
      
       while j < temp:
         #print preLine[preLen]
         sequence += preLine[j] 
         j += 1
         k += 1
       if k < preLen and j >= temp: # if just 1 previous line is not enough
           index = buffer.index(preLine)
           preLine = buffer[index-1]
           gap = preLen - k
       if k >= preLen:
      	   preFlag = False
     
    current = count
    i = 0
    while current <= end and current > start and i < len(line):
        #print line[i]
        sequence += line[i]
        current += 1
        i += 1
        #print len(sequence)
        #print "Current:", current
     #print len(sequence)
   count += len(line)
   preLine = line
 print len(sequence)
 return sequence
 

script, readFile, writeFile = argv

target1 = open(readFile, 'r')

target2 = open(writeFile, 'w')
buffer = []
keep = False
for line in target1:
	if line.startswith(">chr"):
		if line.startswith(">chr21"):
			keep = True
		else:
			keep = False
	elif keep:
		buffer.append(line)		

cache = buffer
BPtm = 42880007
TMend = 42903043

seq1 = extract(BPtm, TMend, cache)
rSeq1 = seq1[::-1]
# print "seq1 is ", seq1
# print "rSeq1 is ", rSeq1
BPerg = 39751949
ERGend = 40033704

seq2 = extract(BPerg, ERGend, cache)
rSeq2 = seq2[::-1]

sequence = rSeq1 + rSeq2
sequence.replace("\n", "")
print "length is ", len(sequence)
# print "seq is ", sequence
# Build a fasta file by formatting TMPRSS2-ERG sequence:
target2.write(">vrTE\n") # reference nae
list = textwrap.wrap(sequence, width=60)
for e in list:
  print e
  target2.write(e)
#target2.write(sequence)
#textwrap.fill(target2, width=60)

'''
c = 0
line = ""
for b in sequence:
   line += b
   c += 1
   if c == 60: 
   	 # print line
  	 target2.write(line)
  	 target2.write("\n")
 	 c = 0
   	 line = ""
target2.write(line)
# target2.write("".join(buffer))
'''
target1.close()
target2.close()
