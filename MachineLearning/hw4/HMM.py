import string, os, sys
import random
from math import *
import numpy

# get file name                                                                 
myfile = 'test.txt'

# f = open(myfile, 'r')

# Get clean word list
with open(myfile) as f:
    words = []
    text = f.read()
    for char in text:
        if char != "\n":
            words.append(char)

# Letter occurance dictionary
occurances = {
    "a" : 0.0,
    "b" : 0.0,
    "c" : 0.0,
    "d" : 0.0,
    "e" : 0.0,
    "f" : 0.0,
    "g" : 0.0,
    "h" : 0.0,
    "i" : 0.0,
    "j" : 0.0,
    "k" : 0.0,
    "l" : 0.0,
    "m" : 0.0,
    "n" : 0.0,
    "o" : 0.0,
    "p" : 0.0,
    "q" : 0.0,
    "r" : 0.0,
    "s" : 0.0,
    "t" : 0.0,
    "u" : 0.0,
    "v" : 0.0,
    "w" : 0.0,
    "x" : 0.0,
    "y" : 0.0,
    "z" : 0.0,
    " " : 0.0
}

for l in words:
    occurances[l] += 1

# Now build HMM: initial parameters
omega = []
pi = []
theta = []
n_states = int(sys.argv[1])
min_p = -1 * 2**20

# Initialize HMM with randomly generated pi, transtion and emission values
def initialize():
    sum_p = 0.0
    for state1 in range(n_states):
         
        # Pi probabilities
        pi.append(random.random())
        sum_p += pi[state1]

        # Store state transition probabilities
        sum_t = 0.0
        row_t = []
        for index in range(n_states):
            row_t.append(random.random())
            sum_t += row_t[index]
        for state2 in range(n_states):
            row_t[state2] /= sum_t
            row_t[state2] = numpy.log(row_t[state2]) 
        theta.append(row_t) 
        

        # Emission probabilities
        sum_e = 0.0
        row_e = {}
        for l in occurances.keys():
            row_e[l] = random.random()
            sum_e += row_e[l] 
        for l in occurances.keys():
            row_e[l] /= sum_e
            row_e[l] = numpy.log(row_e[l])
        omega.append(row_e)

    for i in range(n_states):
        pi[i] /= sum_p
        pi[i] = numpy.log(pi[i])



# Forward algorithm generating trellis. 
def alpha_trellis(observed, init, trans, em):
    # for storage in matrix [t][state] 
    trellis = []
    curr = []

    # Initalize trellis for t = 0.0
    for x in range(n_states):
        curr.append(init[x] + em[x][observed[0]])
    trellis.append(curr)
 
    for y in observed[1:]:
        prev = curr
        curr = []
        for x_t in range(n_states):
            val = trans[0][x_t] + prev[0] + em[x_t][y]
            for x_tm1 in range(1, n_states):                    
                nu = trans[x_tm1][x_t] + prev[x_tm1] + em[x_t][y]
                try:
                    val += numpy.log(1 + exp(nu - val))
                except:
                    val += min_p
                    print "OVERFLOW"
            curr.append(val)

        # Append alpha values for all states at current t to trellis
        trellis.append(curr)

    return trellis



# Backward algorithm generating trellis.
def beta_trellis(observed, trans, em):
    # for storage in matrix [t][state]
    trellis = []
    curr = []
    rev_observed = observed[::-1]

    # Initalize trellis for the last time step
    for x in range(n_states):
        curr.append(0.0)
    trellis.append(curr)

    # loop backwards though time points, will end with inital states!
    for t in range(1, len(observed)):
        next_t = curr
        curr = []
        for x_t in range(n_states):
            val = trans[x_t][0] + em[0][rev_observed[t-1]] + next_t[0]
            for x_tp1 in range(1, n_states):
                nu = trans[x_t][x_tp1] + em[x_tp1][rev_observed[t-1]] + next_t[x_tp1]
                try:
                    val += numpy.log(1 + exp(nu - val))
                except:
                    val += min_p
                    print "OVERFLOW"
            curr.append(val)

        # Append beta values for all states at current t to trellis. Since going backwards, append to front
        trellis.insert(0, curr)

    return trellis



def gamma_trellis(alpha, beta, t_len):
    trellis = []

    for t in range(t_len):
        curr = []
        ttot = alpha[t][0] + beta[t][0]
        curr.append(ttot)
        for x_t in range(1, n_states):
            val = alpha[t][x_t] + beta[t][x_t]
            ttot += numpy.log(1 + exp(val - ttot))
            curr.append(val)
        for i in range(n_states):
            curr[i] -= ttot
        trellis.append(curr)

    return trellis
    


def xi_trellis(gamma, beta, trans, em, observed):
    trellis = []
    for t in range(len(observed)-1):
        curr = []
        for x_t in range(n_states):
            row = []
            val = gamma[t][x_t] - beta[t][x_t]
            for x_tp1 in range(n_states):
                row.append(val + beta[t+1][x_tp1] + trans[x_t][x_tp1] + em[x_tp1][observed[t+1]])
            curr.append(row)
        trellis.append(curr)

    return trellis



def update(pi, omega, theta, gamma, observed, xi):
    #import ipdb; ipdb.set_trace()
    for i in range(n_states):
        # Update pi
        pi[i] = gamma[0][i]

        # Update omega
        denom = gamma[0][i]
        for t in range(1, len(observed)):
            denom += numpy.log(1 + exp(gamma[t][i] - denom))
        for letter in occurances.keys():
            nom = 0.0
            for t,y in enumerate(observed):
                if y == letter:
                    if nom == 0.0:
                        nom = gamma[t][i]
                    else:
                        nom += numpy.log(1 + exp(gamma[t][i] - nom))
            omega[i][letter] = nom - denom
  
        # Update theta
        denom = gamma[0][i]
        for t in range(1, len(observed)-1):
            denom += numpy.log(1 + exp(gamma[t][i] - denom))
        for j in range(n_states):
            nom = xi[0][i][j]
            for t in range(1, len(observed)-1):
                try:
                    nom += numpy.log(1 + exp(xi[t][i][j] - nom))
                except:
                    nom += min_p
            theta[i][j] = nom - denom



# Forward algorithm generating trellis. 
def repair_alpha(observed, init, trans, em):
    # for storage in matrix [t][state] 
    trellis = []
    curr = []

    # Initalize trellis for t = 0.0
    for x in range(n_states):
        curr.append(init[x] + em[x][observed[0]])
    trellis.append(curr)
 
    for t, y in enumerate(observed[1:]):
        prev = curr
        curr = []
        if (y == "*"):
            for x_t in range(n_states):
                val = trans[0][x_t] + prev[0]
                for x_tm1 in range(1, n_states):                    
                    nu = trans[x_tm1][x_t] + prev[x_tm1]
                    val += numpy.log(1 + exp(nu - val))
                curr.append(val)
        else:
            for x_t in range(n_states):
                val = trans[0][x_t] + prev[0] + em[x_t][y]
                for x_tm1 in range(1, n_states):                    
                    nu = trans[x_tm1][x_t] + prev[x_tm1] + em[x_t][y]
                    val += numpy.log(1 + exp(nu - val))
                curr.append(val)

        # Append alpha values for all states at current t to trellis
        trellis.append(curr)

    return trellis


# Backward algorithm generating trellis.
def repair_beta(observed, trans, em):
    # for storage in matrix [t][state]
    trellis = []
    curr = []
    rev_observed = observed[::-1]

    # Initalize trellis for the last time step
    for x in range(n_states):
        curr.append(0.0)
    trellis.append(curr)

    # loop backwards though time points, will end with inital states!
    for t in range(1, len(observed)):
        next_t = curr
        curr = []
        if rev_observed[t-1] == "*":
            for x_t in range(n_states):
                val = trans[x_t][0] + next_t[0]
                for x_tp1 in range(1, n_states):
                    nu = trans[x_t][x_tp1] + next_t[x_tp1]
                    val += numpy.log(1 + exp(nu - val))
                curr.append(val)
        else:
            for x_t in range(n_states):
                val = trans[x_t][0] + em[0][rev_observed[t-1]] + next_t[0]
                for x_tp1 in range(1, n_states):
                    nu = trans[x_t][x_tp1] + em[x_tp1][rev_observed[t-1]] + next_t[x_tp1]
                    val += numpy.log(1 + exp(nu - val))
                curr.append(val)


        # Append beta values for all states at current t to trellis. Since going backwards, append to front
        trellis.insert(0, curr)

    return trellis



def repair1(alpha, beta, em, m):
    maxp = -1 * 2**30
    for letter in occurances.keys():
        tot = em[0][letter] + beta[m][0] + alpha[m][0]
        for x in range(1, n_states):
            val = em[x][letter] + beta[m][x] + alpha[m][x]
            try:
                tot += numpy.log(1 + exp(val - tot))
            except:
                tot += min_p
        if tot > maxp:
            maxp = tot
            maxl = letter
    return maxl



def repair(init, trans, em):
    missing = []
    with open("corrupted.txt") as f:
        text = []
        work = f.read()
        for i,char in enumerate(work):
            if char != "\n":
                text.append(char)
                if char == "*":
                    missing.append(i)

    #print missing
    #print len(missing)
    a = repair_alpha(text, init, trans, em)
    b = repair_beta(text, trans, em)

    #print a
    #print b

    repairs = []
    for m in missing:
        repairs.append(repair1(a, b, em, m))

    correct = list("e sccyil meesh eh usseqotibuhnese torfn f ihhglhaw  eo c wsie e ig idu  ocer nhiny e nhc")
    err = 0
    for i,l in enumerate(missing):
        if repairs[i] != correct[i]:
            print "Error! idx = "+str(l), "got", str(repairs[i]), "want", str(correct[i])
            err += 1

    print "ERRORS =", str(err)
    print repairs

    for i,m in enumerate(missing):
        text[m] = repairs[i]

    out = open("corrected.txt", "w")
    out.write(''.join(text))


def p(alpha, observed):
    le = len(observed)-1
    tot = alpha[le][0]
    for x in range(1, n_states):
        tot += log(1 + exp(alpha[le][x] - tot))

    return tot



def hmm():
    initialize()

    # Iterate
    for i in range(1):
        alpha = alpha_trellis(words, pi, theta, omega)
        beta = beta_trellis(words, theta, omega)
        gamma = gamma_trellis(alpha, beta, len(words))
        xi = xi_trellis(gamma, beta, theta, omega, words)
        update(pi, omega, theta, gamma, words, xi)
        #print p(alpha, words)
        #print beta
        print i





hmm()
#repair(pi, theta, omega)

#print 'Initial state probabilities:'
print pi
#print 'State transition probabilities:'
#print theta
#print 'Emission probabilities:'
#print omega

#for key, value in sorted(omega[0].iteritems(), key=lambda (k,v): (v,k), reverse=True):
#    print "%s: %s" % (key, value)

#for i in range(n_states):
#    thing = sorted(omega[i].iteritems(), key=lambda (k,v): (v,k), reverse=True)
#    print "~~~~~~~~~~~~~~~~~~~STATE" + str(i)
#    for j in range(27):
#        print thing[j]


def mostLikely(item):
    return sorted(item.iteritems(),key=lambda (k,v): (v,k), reverse=True)[0]

    
