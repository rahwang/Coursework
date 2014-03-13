import csv
import sys
from pylab import *
from numpy import *
from scipy import *
from scipy import optimize
import matplotlib.pyplot as plt

plt.ylabel("Likelihood of Training Data (in log form)")
plt.xlabel("# of States")

n = range(1,21)

ps = []

with open("data.txt", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        ps.append(float(row[2]))

# Create plots with pre-defined labels.
# Alternatively, you can pass labels explicitly when calling `legend`.
#fig, ax = plt.subplots()

plt.plot(n, ps, 'k')
#for l, c, mu in zip(ls, cs, mus):
#    plt.plot(ts, l, c, label='mu = '+str(mu))

# Now add the legend with some customizations.
#legend = plt.legend(loc='best', shadow=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
#frame  = legend.get_frame()
#frame.set_facecolor('0.90')

#plt.xscale('log', basey=2)
#plt.yscale('log')

# Set the fontsize
#for label in legend.get_texts():
#    label.set_fontsize('small')

#for label in legend.get_lines():
#    label.set_linewidth(1.5)  # the legend line width

#plt.title("Linear Online Errors")
plt.title("States vs Likelihood")

plt.show()

savefig("p2.png")

