import string, os, sys

# get file                                                                
data = open('Simple_Brown.txt', 'r')

# get corpus and gold standard as lists           
words = []
for line in data:
    nu = line.replace(" ", "")
    nu = nu.replace("\n", "")
    words.append(nu)

p_occur = {}
s_occur = {}

# Collect occurances of four letter strings
for word in words:
    l = len(word)
    if l < 5:
        continue;
    pre1 = word[0:3]
    pre2 = word[0:4] 
    suf1 = word[(l-3):]
    suf2 = word[(l-4):]
    if pre1 not in p_occur.keys():
        p_occur[pre1] = 1
    else:
        p_occur[pre1] += 1
    if pre2 not in p_occur.keys():
        p_occur[pre2] = 1
    else:
        p_occur[pre2] += 1
    if suf1 not in s_occur.keys():
        s_occur[suf1] = 1
    else:
        s_occur[suf1] += 1
    if suf2 not in s_occur.keys():
        s_occur[suf2] = 1
    else:
        s_occur[suf2] += 1

prefixes = []
for s in p_occur.keys():
    if (len(s) == 3 and p_occur[s] >= 15) or (len(s) == 4 and p_occur[s] >= 10):
        if s in words:
            prefixes.append(s)
            #print s

suffixes = []
for s in s_occur.keys():
    if (len(s) == 3 and s_occur[s] >= 15) or (len(s) == 4 and s_occur[s] >= 10):
        if s in words:
            suffixes.append(s)
            print s


