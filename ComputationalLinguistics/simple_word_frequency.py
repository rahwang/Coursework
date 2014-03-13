import string, os, sys

# get file name                                                                 
myfile = 'voy.b.txt'

f = open(myfile, 'r')

# get list of words, then strip punctuation, caps and empty elements           
words = []
for line in f:
    words.extend(line.split())

#Word-Occurance Dictionary                                                     
occur_d = {}

# add/increment words in dictionaries
for word in words:
    if word in occur_d.keys():
        occur_d[word] += 1
    else:
        occur_d[word] = 1

# print all entries
for word in occur_d.keys():
    print str(occur_d[word])
