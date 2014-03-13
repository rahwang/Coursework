import string, os, sys
import random
from math import *

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
n_states = 2

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
            row_t[state2] = log(row_t[state2]) 
        theta.append(row_t) 
        

        # Emission probabilities
        sum_e = 0.0
        row_e = {}
        for l in occurances.keys():
            row_e[l] = random.random()
            sum_e += row_e[l] 
        for l in occurances.keys():
            row_e[l] /= sum_e
            row_e[l] = log(row_e[l])
        omega.append(row_e)

    for i in range(n_states):
        pi[i] /= sum_p
        pi[i] = log(pi[i])



# Forward algorithm generating trellis. 
def alpha_trellis(observed, init, trans, em):
    # for storage in matrix [t][state] 
    trellis = []
    curr = []
    print "ALPHAS"
    # Initalize trellis for t = 0.0
    for x in range(n_states):
        curr.append(init[x] * em[x][observed[0]])
        print "TIME 0 STATE", str(x)
        print str(init[x]), str(em[x][observed[0]]),"=",str(init[x] * em[x][observed[0]])
    trellis.append(curr)
 
    for i, y in enumerate(observed[1:]):
        prev = curr
        curr = []
        for x_t in range(n_states):
            val = trans[0][x_t] * prev[0] * em[x_t][y]
            print "TIME",str(i),"STATE", str(x_t)
            print str(trans[0][x_t]), str(prev[0]), str(em[x_t][y]),"+",
            for x_tm1 in range(1, n_states):                    
                nu = trans[x_tm1][x_t] * prev[x_tm1] * em[x_t][y]
                print str(trans[x_tm1][x_t]), str(prev[x_tm1]), str(em[x_t][y]),
                val += nu
                print "=", str(val)
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

    print "BETAS"
    # Initalize trellis for the last time step
    for x in range(n_states):
        print "TIME T STATE", str(x)
        curr.append(1)
    trellis.append(curr)

    # loop backwards though time points, will end with inital states!
    for t in range(1, len(observed)):
        next_t = curr
        curr = []
        for x_t in range(n_states):
            val = trans[x_t][0] * em[0][rev_observed[t-1]] * next_t[0]
            print "TIME",str(len(observed)-t-1),"STATE", str(x_t)
            print str(trans[x_t][0]), str(next_t[0]), str(em[0][rev_observed[t-1]]),"+",
            for x_tp1 in range(1, n_states):
                nu = trans[x_t][x_tp1] * em[x_tp1][rev_observed[t-1]] * next_t[x_tp1]
                print str(trans[x_t][x_tp1]), str(next_t[x_tp1]), str(em[x_tp1][rev_observed[t-1]]),"=",
                val += nu
            print val
            curr.append(val)

        # Append beta values for all states at current t to trellis. Since going backwards, append to front
        trellis.insert(0, curr)

    return trellis



def gamma_trellis(alpha, beta, t_len):
    trellis = []
    print "GAMMAS"
    for t in range(t_len):
        curr = []
        ttot = 0.0
        for x_t in range(n_states):
            val = alpha[t][x_t] * beta[t][x_t]
            ttot += val
            curr.append(val)
        for i in range(n_states):
            curr[i] = curr[i]/ttot
            print "TIME", str(t), "STATE", str(i), "=", str(curr[i])
        trellis.append(curr)

    return trellis
    


def xi_trellis(gamma, beta, trans, em, observed):
    print "XIS"
    trellis = []
    for t in range(len(observed)-1):
        curr = []
        for x_t in range(n_states):
            row = []
            val = gamma[t][x_t]/beta[t][x_t]
            for x_tp1 in range(n_states):
                row.append(val * beta[t+1][x_tp1] * trans[x_t][x_tp1] * em[x_tp1][observed[t+1]])
                print "TIME", str(t), "STATES", str(x_t), str(x_tp1), "=", str(val * beta[t+1][x_tp1] * trans[x_t][x_tp1] * em[x_tp1][observed[t+1]])
            curr.append(row)
        trellis.append(curr)

    return trellis



def update(pi, omega, theta, gamma, observed, xi):
    for i in range(n_states):
        # Update pi
        pi[i] = gamma[0][i]

        # Update omega
        denom = gamma[0][i]
        for t in range(1, len(observed)):
            denom += gamma[t][i]
        for letter in ["A","B"]:
            nom = 0.0
            for t,y in enumerate(observed):
                if y == letter:
                    if nom == 0.0:
                        nom = gamma[t][i]
                    else:
                        nom += gamma[t][i]
                omega[i][letter] = nom/denom
  
        # Update theta
        denom = gamma[0][i]
        for t in range(1, len(observed)-1):
            denom += gamma[t][i]
        for j in range(n_states):
            nom = xi[0][i][j]
            for t in range(1, len(observed)-1):
                nom += xi[t][i][j]
            theta[i][j] = nom/denom




def hmm():
    #initialize()

    words = "ABBA"
    pi = [.85, .15]
    omega = [{"A" : .4, "B" : .6}, {"A" : .5, "B" : .5}]
    theta = [[.3, .7], [.1, .9]]
    
    for i in range(2):
        print i
        alpha = alpha_trellis(words, pi, theta, omega)
        beta = beta_trellis(words, theta, omega)
        gamma = gamma_trellis(alpha, beta, len(words))
        xi = xi_trellis(gamma, beta, theta, omega, words)
        update(pi, omega, theta, gamma, words, xi)
        print 
        print "PI"
        print pi
        print 
        print "OMEGA"
        print omega 
        print
        print "THETA"
        print theta

    # Iterate
    #for i in range(50):
     #   alpha = alpha_trellis(words, pi, theta, omega)
      #  beta = beta_trellis(words, theta, omega)
      #  gamma = gamma_trellis(alpha, beta, len(words))
      #  xi = xi_trellis(gamma, beta, theta, omega, words)
      #  update(pi, omega, theta, gamma, words, xi)
      #  print i

hmm()

print 'Initial state probabilities:'
print pi
print ' '
print 'State transition probabilities:'
print theta
print ' '
#print 'Emission probabilities:'
#print omega

#for key, value in sorted(omega[0].iteritems(), key=lambda (k,v): (v,k), reverse=True):
#    print "%s: %s" % (key, value)


def mostLikely(item):
    return sorted(item.iteritems(),key=lambda (k,v): (v,k), reverse=True)[0]

    
