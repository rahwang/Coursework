import csv
import sys
from pylab import *
from numpy import *
from scipy import *
from scipy import optimize
import matplotlib.pyplot as plt

plt.ylabel("# Iterations")
plt.xlabel("Theta value")

mus = [0.0, 0.1, 0.2, 0.3, 0.4]
ts = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
cs = ['r','g','b','m','c']

ls = [[],[],[],[],[]]

with open("data.txt", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        if row[0] == "square.data" and row[1] != "0.100000":
            if float(row[2]) == mus[0]:
                ls[0].append(float(row[4]))
            if float(row[2]) == mus[1]:
                ls[1].append(float(row[4]))
            if float(row[2]) == mus[2]:
                ls[2].append(float(row[4]))
            if float(row[2]) == mus[3]:
                ls[3].append(float(row[4]))
            if float(row[2]) == mus[4]:
                ls[4].append(float(row[4]))

print ls[1]

# Create plots with pre-defined labels.
# Alternatively, you can pass labels explicitly when calling `legend`.
#fig, ax = plt.subplots()

for l, c, mu in zip(ls, cs, mus):
    plt.plot(ts, l, c, label='mu = '+str(mu))

# Now add the legend with some customizations.
legend = plt.legend(loc='best', shadow=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame  = legend.get_frame()
frame.set_facecolor('0.90')

#plt.xscale('log', basey=2)
#plt.yscale('log')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('small')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

#plt.title("Linear Online Errors")
plt.title("Iterations v Theta (square.data)")

plt.show()

savefig("p2.png")

