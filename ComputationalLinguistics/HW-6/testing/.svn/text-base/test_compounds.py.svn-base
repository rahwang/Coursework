import string, os, sys

# get files                                                                
# data = open('Simple_Brown.txt', 'r')
# gold = open('gold_standard.txt', 'r')
# pre = open('stest.txt', 'r')
# suf = open('stest.txt', 'r')

data = open('test_c.txt', 'r')
gold = open('test_g.txt', 'r')
pre = open('test_s.txt', 'r')
# suf = open('stest.txt', 'r')

# get corpus and gold standard as lists           
words = []
for l1 in data:
    tmp = l1.replace("\n", "").replace(" ", "")
    if tmp != "":
        words.append(tmp)
gs = []
for l2 in gold:
    tmp = l2.replace("\n", "")
    if tmp != "":
        gs.append(tmp)
prefixes = []
for l3 in pre:
    tmp = l3.replace("\n", "")
    if tmp != "":
        prefixes.append(tmp)

print prefixes
#suffixes = []
#for line in suf:
#    suffixes.append(l3.replace("\n", ""))

# Compound dictionary, from gold standard
# Stores index of the break
standard = {}
for w in gs:
    val = w.replace(" ", "")
    if val is not None:
        standard[val] = 0
        for i,char in enumerate(w):
            if char == ' ':
                standard[val] += i
                break
            elif char == '-':
                standard[val] += i
                break

print standard

# Algorithm. Break-up words, test both segments for prescence in corpus
compounds = {}
for word in words:
    l = len(word)
    compounds[word] = 0
    for i,char in enumerate(word):
        if char == '-':
            compounds[word] = i
            print word
            break
        if l > 5 and i > 2 and i < (l-2):
            p1 = word[0:i]
            p2 = word[i:l]
            if (p1 not in prefixes): 
                if (p2 not in suffixes):
                    if (p1 in gs) and (p2 in gs):
                        compounds[word] = i
                        print p1 + ' ' + p2
                        break

# Check precision and recall
tot_t_pos = 0.0
tot_pos_claimed = 0.0
found_t_pos = 0.0
for word in words:
    if word in standard.keys():
        std = standard[word]
        com = compounds[word]
        if std > 0:
            tot_t_pos += 1
            if std == com:
                found_t_pos += 1
        if com > 0:
            tot_pos_claimed += 1

print ' '
print str(tot_t_pos)
print str(tot_pos_claimed)
print str(found_t_pos)
print ' '
print 'Precision: ' + str(found_t_pos/tot_pos_claimed)
print 'Recall: ' + str(found_t_pos/tot_t_pos)
